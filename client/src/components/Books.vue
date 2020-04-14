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
							<router-link :to="`/order/${book.id}`" class="button rent">Rent</router-link>
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

<style scoped>

 #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  margin: 0 auto;
  margin-top: 60px;
  padding: 10px 20px;

  min-width: 60px;
  width: fit-content;
  border-radius: 15px;

  background-color: rgb(226, 208, 202);
  color: darkcyan;

}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}


/* --------------Books---------------- */
.table-wrap {
  display: flex;
  flex-direction: column;

  padding: 20px;

  border: 2px solid darkslategrey
}

.table-wrap > h1 {
  width: 75vw;
  text-align: left;
}

/* -----------------Product table buttons------------------------- */
.button-group {
	display: flex;
	flex-direction: column;
	justify-content: space-around;
	align-items: flex-end;
}

.table-wrap .button,
.table-wrap .button .rent {
	display: block;
	flex-grow: 1;
  margin: 5px 5px;
  padding: 10px 20px;

	width: 15ch;
  /* width: fit-content; */

	font-size: 14px;

  border: none;
  border-radius: 10px;

  cursor: pointer;
}

.add {
  background-color: rgb(16, 150, 139);
}

.update {
  background-color: rgb(155, 109, 207);
}

.delete {
  background-color: crimson;
}
/* Since Rent is actually a router-link that generates an achor tag from an endpoint and product ID, it will require some*/
 /*separate, special styling, though it is under the button section, because functionally, it will have the same purpose  */
.rent {
	box-sizing: border-box;
	/* display: block; */
	text-decoration: none;
	color: black;
	background-color: deeppink;
}
/* -------------------------------------------------------------------------------------- */

.table {
  display: flex;
  flex-direction: column;
}
thead,
tbody {
  display: flex;
}

tbody {
  flex-direction: column;
}

.table tr {
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 1;

  padding: 10px 0;
  border-top: 1px darkslategrey solid;
}

thead > tr > th,
tbody > tr > td {
 flex: 1;
 /* margin: auto; */
}

/* ----------modal Styling ---------------- */

	.modal-open .modal {
		overflow-x: hidden;
		overflow-y: auto;
	}
/* Ensure that the modal covers the entirety of the screen without budge */
	.modal {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		outline: none;
	}

/* Establish the transition timing for background transparency */
	.fade {
		transition: all .1s linear;
		transition-delay: 0s;
	}
/* When then Add/Update button is clicked, this class is appended to the element, triggering the modal box, and casting an overlay to the bg */
/* NOTE_____ I need to find a way to fix the transition to occur in tandem with the modal appearing, not after. */
	.show {
		background-color: hsla(270deg, 0%, 10%, 0.5);
		transition-delay: 0s;
	}

	.modal.fade .modal-dialog {
		transform: translateY(-50px);
		transition: all .1s linear;
		transition-delay: 0s;
		opacity: 0;
	}

	.modal.show .modal-dialog {
		transform: none;
		opacity: 1;
	}

	.modal-dialog {
		position: relative;

		margin: 20vh auto;
		max-width: 500px;

		text-align: left;
		pointer-events: none;
	}

	.modal-content {
		position: relative;
		display: flex;
		flex-direction: column;
		width: 100%;
		pointer-events: auto;
		background: rgb(239,85,44);
		background: linear-gradient(180deg, rgba(239,85,44,1) 0%, rgba(247,189,52,1) 100%);
		background-clip: padding-box;
		border: 1px outset #ec5920;
		border-radius: 7px;
		color: black;
	}

	.modal-header {
		display: flex;
		justify-content: space-between;
		align-items: center;

		padding: 1rem;
		border-bottom: 1px solid darkslategrey;
	}

	.modal-title {
		margin: 0;
		/* padding:; */
		font-size: 1rem;
	}

	.close {
		background: none;
		border: none;

		font-size: 2rem;

		cursor: pointer;

		transition: all .1s ease-in;
	}

	.close:hover {
		color: darkslategray;
		transform: scale(1.25);
	}

	.modal-body {
		padding: 1rem;
	}

	.form-group {
		display: flex;
		align-items: center;
		padding: .5rem 0;
	}

	.form-group > div {
		display: flex;
		flex:1;
	}

	.form-group > label {
		min-width: 10ch;
		font-size: 1rem;
	}

	.form-group > div > .form-control {
		display: block;
		flex: 1;

		padding: .5rem;

		font-size: 1rem;

		background: rgba(0, 0, 0, 0.2);
		border: none;
		border-bottom: 5px outset rgba(0, 0, 0, 0.2);
		border-left: 5px outset rgba(0, 0, 0, 0.2);
		border-radius: 20px;

		outline: rgba(0,0,0,0);
	}

	.form-group > div > .form-control::placeholder {
		color: black;
	}

	fieldset.form-group {
		border: none;
		padding: 1rem 0;
	}

	.modal-content .btn {
		padding: .5rem;
		margin: .75rem 1rem .5rem 0;
		min-width: 10ch;

		font-size: 1rem;

		/* background: linear-gradient(180deg, rgba(239,85,44,1) 0%, rgba(247,189,52,1) 100%); */
		/* border: 3px outset rgba(239,85,44,1); */
		background: rgba(0, 0, 0, 0.4);
		border: none;
		border-radius: 15px;
		/* box-shadow: 2px 2px 3px 1px rgba(0, 0, 0, 0.4); */

		cursor: pointer;

		transition: all .2s ease-in;
	}

	.modal-content .btn-primary:hover {
		background: rgba(247,189,52,1);
		box-shadow: 2px 2px 3px 1px rgba(0, 0, 0, 0.4);
		transform: translate(-.05rem, -.05rem);
	}

	.modal-content .btn-danger:hover {
		background: rgba(239,85,44,1);
		box-shadow: 2px 2px 3px 1px rgba(0, 0, 0, 0.4);
		transform: translate(-.05rem, -.05rem);
	}

</style>
