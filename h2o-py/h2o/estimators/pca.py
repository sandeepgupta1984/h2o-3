#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric


class H2OPrincipalComponentAnalysisEstimator(H2OEstimator):
    """
    Principal Components Analysis

    """

    algo = "pca"

    def __init__(self, **kwargs):
        super(H2OPrincipalComponentAnalysisEstimator, self).__init__()
        self._parms = {}
        names_list = {"model_id", "training_frame", "validation_frame", "ignored_columns", "ignore_const_cols",
                      "score_each_iteration", "transform", "pca_method", "pca_impl", "k", "max_iterations",
                      "use_all_factor_levels", "compute_metrics", "impute_missing", "seed", "max_runtime_secs",
                      "export_checkpoints_dir"}
        if "Lambda" in kwargs: kwargs["lambda_"] = kwargs.pop("Lambda")
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in names_list:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))

    @property
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``H2OFrame``.
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        assert_is_type(training_frame, None, H2OFrame)
        self._parms["training_frame"] = training_frame


    @property
    def validation_frame(self):
        """
        Id of the validation data frame.

        Type: ``H2OFrame``.
        """
        return self._parms.get("validation_frame")

    @validation_frame.setter
    def validation_frame(self, validation_frame):
        assert_is_type(validation_frame, None, H2OFrame)
        self._parms["validation_frame"] = validation_frame


    @property
    def ignored_columns(self):
        """
        Names of columns to ignore for training.

        Type: ``List[str]``.
        """
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns


    @property
    def ignore_const_cols(self):
        """
        Ignore constant columns.

        Type: ``bool``  (default: ``True``).
        """
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols


    @property
    def score_each_iteration(self):
        """
        Whether to score during each iteration of model training.

        Type: ``bool``  (default: ``False``).
        """
        return self._parms.get("score_each_iteration")

    @score_each_iteration.setter
    def score_each_iteration(self, score_each_iteration):
        assert_is_type(score_each_iteration, None, bool)
        self._parms["score_each_iteration"] = score_each_iteration


    @property
    def transform(self):
        """
        Transformation of training data

        One of: ``"none"``, ``"standardize"``, ``"normalize"``, ``"demean"``, ``"descale"``  (default: ``"none"``).
        """
        return self._parms.get("transform")

    @transform.setter
    def transform(self, transform):
        assert_is_type(transform, None, Enum("none", "standardize", "normalize", "demean", "descale"))
        self._parms["transform"] = transform


    @property
    def pca_method(self):
        """
        Specify the algorithm to use for computing the principal components: GramSVD - uses a distributed computation of
        the Gram matrix, followed by a local SVD; Power - computes the SVD using the power iteration method
        (experimental); Randomized - uses randomized subspace iteration method; GLRM - fits a generalized low-rank model
        with L2 loss function and no regularization and solves for the SVD using local matrix algebra (experimental)

        One of: ``"gram_s_v_d"``, ``"power"``, ``"randomized"``, ``"glrm"``  (default: ``"gram_s_v_d"``).
        """
        return self._parms.get("pca_method")

    @pca_method.setter
    def pca_method(self, pca_method):
        assert_is_type(pca_method, None, Enum("gram_s_v_d", "power", "randomized", "glrm"))
        self._parms["pca_method"] = pca_method


    @property
    def pca_impl(self):
        """
        Specify the implementation to use for computing PCA (via SVD or EVD): MTJ_EVD_DENSEMATRIX - eigenvalue
        decompositions for dense matrix using MTJ; MTJ_EVD_SYMMMATRIX - eigenvalue decompositions for symmetric matrix
        using MTJ; MTJ_SVD_DENSEMATRIX - singular-value decompositions for dense matrix using MTJ; JAMA - eigenvalue
        decompositions for dense matrix using JAMA. References: JAMA - http://math.nist.gov/javanumerics/jama/; MTJ -
        https://github.com/fommil/matrix-toolkits-java/

        One of: ``"mtj_evd_densematrix"``, ``"mtj_evd_symmmatrix"``, ``"mtj_svd_densematrix"``, ``"jama"``.
        """
        return self._parms.get("pca_impl")

    @pca_impl.setter
    def pca_impl(self, pca_impl):
        assert_is_type(pca_impl, None, Enum("mtj_evd_densematrix", "mtj_evd_symmmatrix", "mtj_svd_densematrix", "jama"))
        self._parms["pca_impl"] = pca_impl


    @property
    def k(self):
        """
        Rank of matrix approximation

        Type: ``int``  (default: ``1``).
        """
        return self._parms.get("k")

    @k.setter
    def k(self, k):
        assert_is_type(k, None, int)
        self._parms["k"] = k


    @property
    def max_iterations(self):
        """
        Maximum training iterations

        Type: ``int``  (default: ``1000``).
        """
        return self._parms.get("max_iterations")

    @max_iterations.setter
    def max_iterations(self, max_iterations):
        assert_is_type(max_iterations, None, int)
        self._parms["max_iterations"] = max_iterations


    @property
    def use_all_factor_levels(self):
        """
        Whether first factor level is included in each categorical expansion

        Type: ``bool``  (default: ``False``).
        """
        return self._parms.get("use_all_factor_levels")

    @use_all_factor_levels.setter
    def use_all_factor_levels(self, use_all_factor_levels):
        assert_is_type(use_all_factor_levels, None, bool)
        self._parms["use_all_factor_levels"] = use_all_factor_levels


    @property
    def compute_metrics(self):
        """
        Whether to compute metrics on the training data

        Type: ``bool``  (default: ``True``).
        """
        return self._parms.get("compute_metrics")

    @compute_metrics.setter
    def compute_metrics(self, compute_metrics):
        assert_is_type(compute_metrics, None, bool)
        self._parms["compute_metrics"] = compute_metrics


    @property
    def impute_missing(self):
        """
        Whether to impute missing entries with the column mean

        Type: ``bool``  (default: ``False``).
        """
        return self._parms.get("impute_missing")

    @impute_missing.setter
    def impute_missing(self, impute_missing):
        assert_is_type(impute_missing, None, bool)
        self._parms["impute_missing"] = impute_missing


    @property
    def seed(self):
        """
        RNG seed for initialization

        Type: ``int``  (default: ``-1``).
        """
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed


    @property
    def seed_string(self):
        """
        RNG seed for initialization as string

        Type: ``str``  (default: ``"-1"``).
        """
        if self._parms.get("seed") is not None: return str(self._parms.get("seed"))
        return None

    @property
    def max_runtime_secs(self):
        """
        Maximum allowed runtime in seconds for model training. Use 0 to disable.

        Type: ``float``  (default: ``0``).
        """
        return self._parms.get("max_runtime_secs")

    @max_runtime_secs.setter
    def max_runtime_secs(self, max_runtime_secs):
        assert_is_type(max_runtime_secs, None, numeric)
        self._parms["max_runtime_secs"] = max_runtime_secs


    @property
    def export_checkpoints_dir(self):
        """
        Automatically export generated models to this directory.

        Type: ``str``.
        """
        return self._parms.get("export_checkpoints_dir")

    @export_checkpoints_dir.setter
    def export_checkpoints_dir(self, export_checkpoints_dir):
        assert_is_type(export_checkpoints_dir, None, str)
        self._parms["export_checkpoints_dir"] = export_checkpoints_dir



    def init_for_pipeline(self):
        """
        Returns H2OPCA object which implements fit and transform method to be used in sklearn.Pipeline properly.
        All parameters defined in self.__params, should be input parameters in H2OPCA.__init__ method.

        :returns: H2OPCA object
        """
        import inspect
        from h2o.transforms.decomposition import H2OPCA
        # check which parameters can be passed to H2OPCA init
        var_names = list(dict(inspect.getmembers(H2OPCA.__init__.__code__))['co_varnames'])
        parameters = {k: v for k, v in self._parms.items() if k in var_names}
        return H2OPCA(**parameters)
