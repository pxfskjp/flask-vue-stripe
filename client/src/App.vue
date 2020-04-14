<template>
  <div id="app">
	<Navigation></Navigation>
    <router-view/>
	<Footer></Footer>
  </div>
</template>

<script>
import Navigation from './components/Navigation.vue';
import Footer from './components/Footer.vue';

<<<<<<< Updated upstream
.table-wrap .button {
  margin: 10px 5px;
  padding: 10px 20px;

  width: fit-content;

  border: none;
  border-radius: 10px;

  cursor: pointer;
}

.add {
  background-color: rgb(16, 150, 139);
}

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
=======
export default {
	name: 'app',
	components: {
		Navigation,
		Footer,
	},
};
</script>


<style>
>>>>>>> Stashed changes

#app {
	margin: 0 auto;
	font-family: Avenir, Helvetica, Arial, sans-serif;
	text-align: center;
	min-width: 60px;
}

h1 {
	margin-top: 4rem;
}

<<<<<<< Updated upstream
.update {
  background-color: rgb(155, 109, 207);
}

.delete {
  background-color: crimson;
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


=======
>>>>>>> Stashed changes
</style>
