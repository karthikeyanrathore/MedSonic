<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">MedSonic</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <router-link to="Heart" class="nav-item nav-link" active-class="active" exact>
            Heart
          </router-link>
          <router-link to="Diabetes" class="nav-item nav-link" active-class="active" exact>
            Diabetes
          </router-link>
          <router-link to="Pneumonia" class="nav-item nav-link" active-class="active" exact>
            Pneumonia
          </router-link>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {}
</script>

<style scoped></style>
