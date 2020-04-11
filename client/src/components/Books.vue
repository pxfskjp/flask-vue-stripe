<template>
  <article class="table-wrap">
    <h1>Games</h1>
    <!-- Referencing the Alert.vue component -->
    <alert :message="message" v-if="showMessage"></alert>
    <button type="button" class="button add" v-b-modal.book-modal>Add Game</button>
    <table class="table">
      <thead>
        <tr>
          <th>Title</th>
          <th>Publisher</th>
          <th>In Stock?</th>
          <th>Rental Price</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(book, index) in books" :key="index">
          <td>{{ book.title }}</td>
          <td>{{ book.publisher }}</td>
          <td>
            <span v-if="book.instock">Yes</span>
            <span v-else>No</span>
          </td>
          <td>${{ book.price }}</td>
          <td>
            <div class="button-group">
              <button type="button" class="button update" v-b-modal.book-update-modal @click="editBook(book)">Update</button>
              <button type="button" class="button delete" @click="onDeleteBook(book)">Delete</button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Add book modal, using this poopy-ass vue-bootstrap nonsense -->
    <b-modal ref="addBookModal"
             id="book-modal"
             title="Add a new game"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-title-group"
                      label="Title:"
                      label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addBookForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Publisher:"
                      label-for="form-author-input">
          <b-form-input id="form-author-input"
                        type="text"
                        v-model="addBookForm.publisher"
                        required
                        placeholder="Enter publisher">
          </b-form-input>
        </b-form-group>
				<b-form-group id="form-price-group"
                      label="Price:"
                      label-for="form-price-input">
          <b-form-input id="form-price-input"
                      type="number"
											step="0.01"
                      v-model="addBookForm.price"
                      required
                      placeholder="Enter price">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-instock-group">
          <b-form-checkbox-group v-model="addBookForm.instock" id="form-checks">
            <b-form-checkbox value="true">In Stock?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>


    <!-- Edit bookywooky -->
    <b-modal ref="editBookModal"
             id="book-update-modal"
             title="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-title-edit-group"
                      label="Title:"
                      label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-edit-group"
                      label="Publisher:"
                      label-for="form-author-edit-input">
          <b-form-input id="form-author-edit-input"
                      type="text"
                      v-model="editForm.publisher"
                      required
                      placeholder="Enter publisher">
          </b-form-input>
        </b-form-group>
				<b-form-group id="form-price-edit-group"
                      label="Price:"
                      label-for="form-price-edit-input">
          <b-form-input id="form-price-edit-input"
                      type="number"
											step="0.01"
                      v-model="editForm.price"
                      required
                      placeholder="Enter price">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-instock-edit-group">
          <b-form-checkbox-group v-model="editForm.instock" id="form-checks">
            <b-form-checkbox value="true">In Stock?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </article>
</template>

<script>
import axios from 'axios';
// import the Alert.Vue component
import Alert from './Alert.vue';

export default {
	data() {
		return {
			books: [],
			addBookForm: {
				title: '',
				publisher: '',
				instock: [],
				price: '',
			},
			editForm: {
				id: '',
				title: '',
				publisher: '',
				instock: [],
				price: '',
			},
			message: '',
			showMessage: false,
		};
	},
	components: {
		alert: Alert,
	},
	methods: {
		getBooks() {
			const path = 'http://localhost:5000/books';
			axios.get(path)
				.then((res) => {
					this.books = res.data.books;
				})
				.catch((error) => {
					// eslint-disable-next-line
          console.error(error);
				});
		},
		addBook(payload) {
			const path = 'http://localhost:5000/books';
			axios.post(path, payload)
				.then(() => {
					this.getBooks();
					// think about how to make the message and showMessage revert after maybe a moment, or at all, really.
					this.message = 'Book added!';
					this.showMessage = true;
				})
				.catch((error) => {
					// eslint-disable-next-line
          console.log(error);
					this.getBooks();
				});
		},
		editBook(book) {
			this.editForm = book;
		},
		initForm() {
			this.addBookForm.title = '';
			this.addBookForm.publisher = '';
			this.addBookForm.instock = [];
			this.addBookForm.price = '';
			this.editForm.id = '';
			this.editForm.title = '';
			this.editForm.publisher = '';
			this.editForm.instock = [];
			this.editForm.price = '';
		},
		onSubmit(evt) {
			evt.preventDefault();
			this.$refs.addBookModal.hide();
			let instock = false;
			if (this.addBookForm.instock[0]) instock = true;
			const payload = {
				title: this.addBookForm.title,
				publisher: this.addBookForm.publisher,
				instock, // property shorthand
				price: this.addBookForm.price,
			};
			this.addBook(payload);
			this.initForm();
		},
		onSubmitUpdate(evt) {
			evt.preventDefault();
			this.$refs.editBookModal.hide();
			let instock = false;
			if (this.editForm.instock[0]) instock = true;
			const payload = {
				title: this.editForm.title,
				publisher: this.editForm.publisher,
				instock,
				price: this.editForm.price,
			};
			this.updateBook(payload, this.editForm.id);
		},
		updateBook(payload, bookID) {
			const path = `http://localhost:5000/books/${bookID}`;
			axios.put(path, payload)
				.then(() => {
					this.getBooks();
					this.message = 'Book updated!';
					this.showMessage = true;
				})
				.catch((error) => {
					// eslint-disable-next-line
          console.error(error);
					this.getBooks();
				});
		},
		removeBook(bookID) {
			const path = `http://localhost:5000/books/${bookID}`;
			axios.delete(path)
				.then(() => {
					this.getBooks();
					this.message = 'Book deleted!';
					this.showMessage = true;
				})
				.catch((error) => {
					// es-lint-disable-next-line
					console.error(error);
					this.getBooks();
				});
		},
		onDeleteBook(book) {
			this.removeBook(book.id);
		},
		onReset(evt) {
			evt.preventDefault();
			this.$refs.addBookModal.hide();
			this.initForm();
		},
		onResetUpdate(evt) {
			evt.preventDefault();
			this.$refs.editBookModal.hide();
			this.initForm();
			this.getBooks(); // why?
		},
	},
	created() {
		this.getBooks();
	},
};
</script>
