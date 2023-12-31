
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "auto_examples\visualizer\plot_performance_curve.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_auto_examples_visualizer_plot_performance_curve.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_auto_examples_visualizer_plot_performance_curve.py:


=========================================================
Plot performance curves
=========================================================

This example illustrates how to use the 
:mod:`imbens.visualizer` module to visualize or 
compare :mod:`imbens.ensemble` classifier(s).

This example uses:

    - :class:`imbens.ensemble.SelfPacedEnsembleClassifier`
    - :class:`imbens.ensemble.EasyEnsembleClassifier`
    - :class:`imbens.ensemble.BalancedRandomForestClassifier`
    - :class:`imbens.ensemble.SMOTEBaggingClassifier`
    - :class:`imbens.visualizer.ImbalancedEnsembleVisualizer`

.. GENERATED FROM PYTHON SOURCE LINES 18-23

.. code-block:: default


    # Authors: Zhining Liu <zhining.liu@outlook.com>
    # License: MIT









.. GENERATED FROM PYTHON SOURCE LINES 24-41

.. code-block:: default

    print(__doc__)

    from time import time

    # Import imbalanced-ensemble
    import imbens

    # Import utilities from sklearn
    import sklearn
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split

    RANDOM_STATE = 42

    # sphinx_gallery_thumbnail_number = 4









.. GENERATED FROM PYTHON SOURCE LINES 42-45

Prepare data
----------------------------
Make a toy 3-class imbalanced classification task.

.. GENERATED FROM PYTHON SOURCE LINES 45-65

.. code-block:: default


    # make dataset
    X, y = make_classification(
        n_classes=3,
        class_sep=2,
        weights=[0.1, 0.3, 0.6],
        n_informative=3,
        n_redundant=1,
        flip_y=0,
        n_features=20,
        n_clusters_per_class=2,
        n_samples=2000,
        random_state=0,
    )

    # train valid split
    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=0.5, stratify=y, random_state=RANDOM_STATE
    )








.. GENERATED FROM PYTHON SOURCE LINES 66-69

Train ensemble classifiers
--------------------------
4 different ensemble classifiers are used.

.. GENERATED FROM PYTHON SOURCE LINES 69-91

.. code-block:: default


    init_kwargs = {'n_estimators': 50, 'random_state': RANDOM_STATE}
    fit_kwargs = {'X': X_train, 'y': y_train}

    # imbens.ensemble classifiers
    ensemble_dict = {
        'SPE': imbens.ensemble.SelfPacedEnsembleClassifier(**init_kwargs),
        'EasyEns': imbens.ensemble.EasyEnsembleClassifier(**init_kwargs),
        'BalanceForest': imbens.ensemble.BalancedRandomForestClassifier(**init_kwargs),
        'SMOTEBagging': imbens.ensemble.SMOTEBaggingClassifier(**init_kwargs),
    }

    # Train all ensemble classifiers, store the results in fitted_ensembles
    fitted_ensembles = {}
    for clf_name, clf in ensemble_dict.items():
        start_time = time()
        clf.fit(**fit_kwargs)
        fit_time = time() - start_time
        fitted_ensembles[clf_name] = clf
        print('Training {:^30s} | Time used: {:.3f}s'.format(clf.__name__, fit_time))






.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    Training  SelfPacedEnsembleClassifier   | Time used: 0.156s
    Training     EasyEnsembleClassifier     | Time used: 0.877s
    Training BalancedRandomForestClassifier | Time used: 0.124s
    Training     SMOTEBaggingClassifier     | Time used: 2.697s




.. GENERATED FROM PYTHON SOURCE LINES 92-97

Fit an ``ImbalancedEnsembleVisualizer``
-----------------------------------------------------
The visualizer fits on a ``dictionary`` like {..., ensemble_name: ensemble_classifier, ...}
The keys should be strings corresponding to ensemble names.
The values should be fitted ``imbalance_ensemble.ensemble`` or ``sklearn.ensemble`` estimator objects.

.. GENERATED FROM PYTHON SOURCE LINES 97-115

.. code-block:: default


    # Initialize visualizer
    visualizer = imbens.visualizer.ImbalancedEnsembleVisualizer(
        eval_datasets={
            'training': (X_train, y_train),
            'validation': (X_valid, y_valid),
        },
        eval_metrics={
            'acc': (sklearn.metrics.accuracy_score, {}),
            'balanced_acc': (sklearn.metrics.balanced_accuracy_score, {}),
            'weighted_f1': (sklearn.metrics.f1_score, {'average': 'weighted'}),
        },
    )

    # Fit visualizer
    visualizer.fit(fitted_ensembles)






.. rst-class:: sphx-glr-script-out

 .. code-block:: none

      0%|                                                                                                                                                                                                                       | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model      SPE      on dataset  training  ::   0%|                                                                                                                                                    | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model      SPE      on dataset  training  :: 100%|#########################################################################################################################################| 50/50 [00:00<00:00, 1515.14it/s]
      0%|                                                                                                                                                                                                                       | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model      SPE      on dataset validation ::   0%|                                                                                                                                                    | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model      SPE      on dataset validation :: 100%|#########################################################################################################################################| 50/50 [00:00<00:00, 1638.71it/s]
      0%|                                                                                                                                                                                                                       | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model    EasyEns    on dataset  training  ::   0%|                                                                                                                                                    | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model    EasyEns    on dataset  training  ::  60%|##################################################################################8                                                       | 30/50 [00:00<00:00, 259.64it/s]    Visualizer evaluating model    EasyEns    on dataset  training  :: 100%|##########################################################################################################################################| 50/50 [00:00<00:00, 202.37it/s]
      0%|                                                                                                                                                                                                                       | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model    EasyEns    on dataset validation ::   0%|                                                                                                                                                    | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model    EasyEns    on dataset validation ::  80%|##############################################################################################################4                           | 40/50 [00:00<00:00, 267.46it/s]    Visualizer evaluating model    EasyEns    on dataset validation :: 100%|##########################################################################################################################################| 50/50 [00:00<00:00, 227.18it/s]
      0%|                                                                                                                                                                                                                       | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model BalanceForest on dataset  training  ::   0%|                                                                                                                                                    | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model BalanceForest on dataset  training  :: 100%|#########################################################################################################################################| 50/50 [00:00<00:00, 2379.94it/s]
      0%|                                                                                                                                                                                                                       | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model BalanceForest on dataset validation ::   0%|                                                                                                                                                    | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model BalanceForest on dataset validation :: 100%|#########################################################################################################################################| 50/50 [00:00<00:00, 2558.16it/s]
      0%|                                                                                                                                                                                                                       | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model SMOTEBagging  on dataset  training  ::   0%|                                                                                                                                                    | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model SMOTEBagging  on dataset  training  :: 100%|#########################################################################################################################################| 50/50 [00:00<00:00, 2173.87it/s]
      0%|                                                                                                                                                                                                                       | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model SMOTEBagging  on dataset validation ::   0%|                                                                                                                                                    | 0/50 [00:00<?, ?it/s]    Visualizer evaluating model SMOTEBagging  on dataset validation :: 100%|#########################################################################################################################################| 50/50 [00:00<00:00, 2000.60it/s]
    Visualizer computing confusion matrices........ Finished!

    <imbens.visualizer.visualizer.ImbalancedEnsembleVisualizer object at 0x000001761BE50970>



.. GENERATED FROM PYTHON SOURCE LINES 116-119

Plot performance curve
----------------------
**Performance w.r.t. number of base estimators**

.. GENERATED FROM PYTHON SOURCE LINES 119-123

.. code-block:: default


    fig, axes = visualizer.performance_lineplot()





.. image-sg:: /auto_examples/visualizer/images/sphx_glr_plot_performance_curve_001.png
   :alt: Performance Curves
   :srcset: /auto_examples/visualizer/images/sphx_glr_plot_performance_curve_001.png
   :class: sphx-glr-single-img





.. GENERATED FROM PYTHON SOURCE LINES 124-127

Set x-axis
----------
(parameter ``n_samples_as_x_axis``: bool)

.. GENERATED FROM PYTHON SOURCE LINES 129-130

**Performance w.r.t. number of training samples**

.. GENERATED FROM PYTHON SOURCE LINES 130-136

.. code-block:: default


    fig, axes = visualizer.performance_lineplot(
        n_samples_as_x_axis=True,
    )





.. image-sg:: /auto_examples/visualizer/images/sphx_glr_plot_performance_curve_002.png
   :alt: Performance Curves
   :srcset: /auto_examples/visualizer/images/sphx_glr_plot_performance_curve_002.png
   :class: sphx-glr-single-img





.. GENERATED FROM PYTHON SOURCE LINES 137-140

Select results for visualization
--------------------------------
(parameter ``on_ensembles``: list of ensemble name, ``on_datasets``: list of dataset name, ``on_metrics``: list of metric name)

.. GENERATED FROM PYTHON SOURCE LINES 142-143

**Select: method ('SPE', 'SMOTEBagging'), data ('validation'), metric ('balanced_acc', 'weighted_f1')**

.. GENERATED FROM PYTHON SOURCE LINES 143-152

.. code-block:: default


    fig, axes = visualizer.performance_lineplot(
        on_ensembles=['SPE', 'EasyEns', 'BalanceForest'],
        on_datasets=['validation'],
        on_metrics=['balanced_acc', 'weighted_f1'],
        n_samples_as_x_axis=True,
    )





.. image-sg:: /auto_examples/visualizer/images/sphx_glr_plot_performance_curve_003.png
   :alt: Performance Curves
   :srcset: /auto_examples/visualizer/images/sphx_glr_plot_performance_curve_003.png
   :class: sphx-glr-single-img





.. GENERATED FROM PYTHON SOURCE LINES 153-156

Customize visual appearance
---------------------------
(parameter ``sub_figsize``: tuple, ``sup_title``: bool or string, kwargs of ``seaborn.lineplot()``)

.. GENERATED FROM PYTHON SOURCE LINES 156-172

.. code-block:: default


    fig, axes = visualizer.performance_lineplot(
        on_ensembles=['SPE', 'EasyEns', 'BalanceForest'],
        on_datasets=['training', 'validation'],
        on_metrics=['balanced_acc', 'weighted_f1'],
        n_samples_as_x_axis=True,
        # Customize visual appearance
        sub_figsize=(3, 4),
        sup_title='My Suptitle',
        # arguments pass down to seaborn.lineplot()
        linewidth=3,
        markers=True,
        alpha=0.8,
    )





.. image-sg:: /auto_examples/visualizer/images/sphx_glr_plot_performance_curve_004.png
   :alt: My Suptitle
   :srcset: /auto_examples/visualizer/images/sphx_glr_plot_performance_curve_004.png
   :class: sphx-glr-single-img





.. GENERATED FROM PYTHON SOURCE LINES 173-176

Group results
-------------
(parameter ``split_by``: list of {'method', 'dataset'})

.. GENERATED FROM PYTHON SOURCE LINES 178-179

**Group results by dataset**

.. GENERATED FROM PYTHON SOURCE LINES 179-190

.. code-block:: default


    fig, axes = visualizer.performance_lineplot(
        on_ensembles=['SPE', 'EasyEns', 'BalanceForest'],
        on_datasets=['training', 'validation'],
        on_metrics=['balanced_acc', 'weighted_f1'],
        n_samples_as_x_axis=True,
        sub_figsize=(3, 2.3),
        split_by=['dataset'],  # Group results by dataset
    )





.. image-sg:: /auto_examples/visualizer/images/sphx_glr_plot_performance_curve_005.png
   :alt: Performance Curves
   :srcset: /auto_examples/visualizer/images/sphx_glr_plot_performance_curve_005.png
   :class: sphx-glr-single-img





.. GENERATED FROM PYTHON SOURCE LINES 191-192

**Group results by method**

.. GENERATED FROM PYTHON SOURCE LINES 192-201

.. code-block:: default


    fig, axes = visualizer.performance_lineplot(
        on_ensembles=['SPE', 'EasyEns', 'BalanceForest'],
        on_datasets=['training', 'validation'],
        on_metrics=['balanced_acc', 'weighted_f1'],
        n_samples_as_x_axis=True,
        sub_figsize=(3, 2.3),
        split_by=['method'],  # Group results by method
    )



.. image-sg:: /auto_examples/visualizer/images/sphx_glr_plot_performance_curve_006.png
   :alt: Performance Curves
   :srcset: /auto_examples/visualizer/images/sphx_glr_plot_performance_curve_006.png
   :class: sphx-glr-single-img






.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  6.163 seconds)


.. _sphx_glr_download_auto_examples_visualizer_plot_performance_curve.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example


    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: plot_performance_curve.py <plot_performance_curve.py>`

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: plot_performance_curve.ipynb <plot_performance_curve.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
