<template>
    <div class="container h-100 p-5">
        <figure class="text-center">
            <h3>
                <u><mark>MedSonic-AI Heart Prediction</mark></u>
            </h3>
        </figure>
        <main class="container">
            <div class="bg-white p-7 rounded">
                <div class="row h-100 justify-content-center align-items-center">
                    <div class="col-50 col-md-20 col-lg-5">
                        <form method="post">
                            <input class="form-control margin-bottom" type="text" name="age" placeholder="age">

                            <input type="text" name="sex" class="form-control margin-bottom" placeholder="sex">

                            <input type="text" name="cp" class="form-control margin-bottom" placeholder="chest pain type">

                            <input type="text" name="trestbps" class="form-control margin-bottom"
                                placeholder="resting blood pressure in mm Hg">

                            <input type="text" name="chol" class="form-control margin-bottom"
                                placeholder="serum cholestoral in mg/dl">

                            <input type="text" name="fbs" class="form-control margin-bottom"
                                placeholder="fasting blood sugar">

                            <input type="text" name="restecg" class="form-control margin-bottom"
                                placeholder="resting electrocardiographic result">

                            <input type="text" name="thalach" class="form-control margin-bottom"
                                placeholder="maximum heart rate achieved">

                            <input type="text" name="exang" class="form-control margin-bottom"
                                placeholder="exercise induced angina">

                            <input type="text" name="oldpeak" class="form-control margin-bottom"
                                placeholder="ST depression">

                            <input type="text" name="slope" class="form-control margin-bottom" placeholder="slope">

                            <input type="text" name="ca" class="form-control margin-bottom"
                                placeholder="number of major vessels ">

                            <input type="text" name="thal" class="form-control margin-bottom" placeholder="thal">

                            <div class="col-md-11 text-center">
                                <button v-on:click="PredictHeartDisease()" type="button"
                                    class="btn btn-primary">Predict</button>
                            </div>
                        </form>
                    </div>
                </div>
                <figure class="text-center">
                    <br>
                    <h3>
                        <mark>Heart Disease Prediction: <strong> {{ result }}</strong></mark>
                    </h3>
                </figure>
            </div>
        </main>
    </div>
</template>
  
<script>
//import axios from "axios"
export default {
    methods: {
        PredictHeartDisease() {
            console.warn("Hi")
        }
    }
}
</script>

<style>
.margin-bottom {
    margin-bottom: 15px;
}
</style>