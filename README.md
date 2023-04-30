<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
  </head>
  <body>
    <h1>Concrete Compressive Strength Prediction</h1>
    <p>This repository contains the code and dataset for predicting the compressive strength of concrete.</p>
    <h2>Data Description</h2>
    <p>The dataset used in this project was acquired from UCI Machine Learning Repository, which can be accessed at https://archive.ics.uci.edu/ml/datasets/Concrete+Compressive+Strength. It comprises 1030 samples and 9 attributes. The attributes consist of 8 inputs and 1 output.</p>
    <p>The inputs include:</p>
    <ul>
      <li>Cement (measured in kg/m3)</li>
      <li>Blast Furnace Slag (measured in kg/m3)</li>
      <li>Fly Ash (measured in kg/m3)</li>
      <li>Water (measured in kg/m3)</li>
      <li>Superplasticizer (measured in kg/m3)</li>
      <li>Coarse Aggregate (measured in kg/m3)</li>
      <li>Fine Aggregate (measured in kg/m3)</li>
      <li>Age (measured in days)</li>
    </ul>
    <p>The output attribute is the Concrete Compressive Strength, which is measured in Mega Pascal (MPa).</p>
    <h2>Installation</h2>
    <ol>
      <li>Clone the repository: <code>git clone https://github.com/ehsanmns/Regression_ConcreteStrength&gt;.git</code></li>
      <li>Install the required packages: <code>pip install -r requirements.txt</code></li>
    </ol>
    <h2>Usage</h2>
    <ol>
      <li>Open the notebook <code>ConcreteStrength.ipynb</code>.</li>
      <li>Run the cells in the notebook to train and evaluate the model.</li>
      <li>Use the trained model to make predictions on new data.</li>
    </ol>
   <h2 dir="auto" tabindex="-1">Modelling and Evaluation</h2>
<ul dir="auto">
<li>
<p dir="auto">Algorithms used</p>
<ul dir="auto">
<li>Linear regression</li>
<li>Lasso regression</li>
<li>Ridge regression</li>
<li>Decision Trees</li>
<li>Random Forests</li>
</ul>
</li>
<li>
<p dir="auto">Metric - As the dependent variable is continuous, RMSE (Root Mean Squared Error) and R2 Score (Coefficient of Determination) have been utilized as evaluation metrics for regression analysis.</p>
<main class="flex-1 overflow-hidden">
<div id="scrollRef" class="h-full overflow-hidden overflow-y-auto p-4">
<div class="w-full max-w-screen-xl m-auto">
<div class="flex w-full mb-6 overflow-hidden">
<div class="overflow-hidden text-sm items-start">
<div class="flex items-end gap-1 mt-2 flex-row">
<div class="flex flex-col">&nbsp;</div>
</div>
</div>
</div>
<div class="sticky bottom-0 left-0 flex justify-center">&nbsp;</div>
</div>
</div>
</main><footer class="p-4">
<div class="w-full max-w-screen-xl m-auto">
<div class="flex items-center justify-between space-x-2">
<div>&nbsp;</div>
<div class="n-auto-complete">
<div class="n-input n-input--textarea n-input--autosize n-input--stateful">
<div class="n-input-wrapper">
<div class="n-input__textarea n-scrollbar" role="none">&nbsp;</div>
</div>
</div>
</div>
</div>
</div>
</footer></li>
</ul>
  </body>
</html>
