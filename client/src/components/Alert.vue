<template>
  <div>
    <b-alert variant="success" show>{{ message }}</b-alert>
  </div>
</template>

<script>
export default {
  props: ['message'],
};
</script>
