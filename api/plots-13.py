import arviz as az
non_centered_data = az.load_arviz_data('non_centered_eight')
fig, axes = az.plot_forest(non_centered_data,
                           kind='forestplot',
                           var_names=['theta'],
                           combined=True,
                           ridgeplot_overlap=3,
                           figsize=(9, 7))
axes[0].set_title('Estimated theta for 8 schools model')