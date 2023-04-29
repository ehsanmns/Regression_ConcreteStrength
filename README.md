<h1>Concrete  Strength Prediction</h1>
<p>This repository contains an example dataset and Python code for predicting cement strength using several features such as cement, blast furnace slag, fly ash, water, super-plasticizer, coarse aggregate, fine aggregate, and age.</p>
<h2>Dataset</h2>
<p>The dataset used in this project is included in the <code>cement_strength_dataset.csv</code> file. It contains 1030 samples with 8 features each and the target set is the strength of the cement. This dataset can be used as a benchmark for those who are new to deep learning.</p>
<h2>Installation</h2>
<p>To use the code in this repository, you need to have the following libraries installed:</p>
<ul>
<li>pandas</li>
<li>numpy</li>
<li>scikit-learn</li>
<li>TensorFlow</li>
</ul>
<p>You can install these libraries using pip:</p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td style="width: 100%;">
<pre class="code-block-wrapper"><code class="hljs code-block-body bash">pip install pandas numpy scikit-learn tensorflow
</code></pre>
</td>
</tr>
</tbody>
</table>
<h2>Usage</h2>
<p>To use the code in this repository, follow these steps:</p>
<ol>
<li>
<p>Clone the repository:</p>
</li>
</ol>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td style="width: 100%;">
<pre class="code-block-wrapper"><code class="hljs code-block-body bash">git <span class="hljs-built_in">clone</span> https://github.com/ehsanmns/cement-strength-prediction.git</code></pre>
</td>
</tr>
</tbody>
</table>
<p>&nbsp; 2. Navigate to the repository directory:</p>
<table style="border-collapse: collapse; width: 100%; height: 18px;" border="1">
<tbody>
<tr style="height: 18px;">
<td style="width: 100%; height: 18px;">
<pre class="code-block-wrapper"><code class="hljs code-block-body bash"><span class="hljs-built_in">cd</span> cement-strength-prediction</code></pre>
</td>
</tr>
</tbody>
</table>
<p>&nbsp; 3. Run the <code>cement_strength_prediction.py</code> script:</p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td style="width: 100%;">
<pre class="code-block-wrapper"><code class="hljs code-block-body bash">python cement_strength_prediction.py
</code></pre>
</td>
</tr>
</tbody>
</table>
<p>This will load the dataset, preprocess it, define a neural network architecture, train the model, and evaluate it on the testing data. The test loss will be printed to the console.</p>
<p>&nbsp; 4.(Optional) Make predictions using the trained model:</p>
<div class="code-block-header">
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td style="width: 100%;">
<pre class="code-block-wrapper"><code class="hljs code-block-body bash">python make_prediction.py
</code></pre>
</td>
</tr>
</tbody>
</table>
</div>
<p>This will load the saved model from the <code>cement_strength_model.h5</code> file, make a prediction on a new sample, and print the predicted strength to the console.</p>
<h2>Acknowledgements</h2>
<p>This dataset was sourced from the Kaggle Website (Pratham Tripathi)</p>
