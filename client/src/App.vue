<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>
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

  padding: 10px 0;
  border-top: 1px darkslategrey solid;
}

thead > tr > th,
tbody > tr > td {
 flex: 1;
 /* margin: auto; */
}

.update {
  background-color: rgb(155, 109, 207);
}

.delete {
  background-color: crimson;
}
</style>
