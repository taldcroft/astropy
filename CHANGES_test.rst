4.0 (unreleased)
================

New Features
------------

astropy.config
^^^^^^^^^^^^^^

astropy.constants
^^^^^^^^^^^^^^^^^

- The version of constants can be specified via ScienceState in a way
  that ``constants`` and ``units`` will be consistent. [#8517]

- Default constants now use CODATA 2018 and IAU 2015 definitions. [#8761]

astropy.convolution
^^^^^^^^^^^^^^^^^^^

astropy.coordinates
^^^^^^^^^^^^^^^^^^^

- Changed ``coordinates.solar_system_ephemeris`` to also accept local files
  as input. The ephemeris can now be selected by either keyword (e.g. 'jpl',
  'de430'), URL or file path. [#8767]

- Added a ``cylindrical`` property to ``SkyCoord`` for shorthand access to a
  ``CylindricalRepresentation`` of the coordinate, as is already available
  for other common representations. [#8857]

astropy.cosmology
^^^^^^^^^^^^^^^^^

astropy.extern
^^^^^^^^^^^^^^

- Remove the bundled ``six`` module. [#8315]

astropy.io.ascii
^^^^^^^^^^^^^^^^

astropy.io.misc
^^^^^^^^^^^^^^^

- Eliminate deprecated compatibility mode when writing ``Table`` metadata to HDF5 format. [#8899]

- Add support for orthogonal polynomial models to ASDF. [#9107]

astropy.io.fits
^^^^^^^^^^^^^^^

- Changed the ``fitscheck`` and ``fitsdiff`` script to use the ``argparse``
  module instead of ``optparse``. [#9148]

astropy.io.registry
^^^^^^^^^^^^^^^^^^^

astropy.io.votable
^^^^^^^^^^^^^^^^^^

astropy.modeling
^^^^^^^^^^^^^^^^

- Major rework of modeling internals.
  See modeling documentation for details.
  `<https://docs.astropy.org/en/latest/modeling/changes_for_4.html>`_ . [#8769]

- Significant reorganization of the documentation. [#9078, #9171]

- Add ``Tabular1D.inverse`` [#9083]
- Significant reorganization of the documentation. [#9078, #9171]

- ``Model.rename`` was changed to add the ability to rename ``Model.inputs``
  and ``Model.outputs``. [#9220]

- New function ``fix_inputs`` to generate new models from others by fixing
  specific inputs variable values to constants. [#9135]


astropy.nddata
^^^^^^^^^^^^^^

astropy.samp
^^^^^^^^^^^^

astropy.stats
^^^^^^^^^^^^^

astropy.table
^^^^^^^^^^^^^

- Improved the implementation of ``Table.replace_column()`` to provide
  a speed-up of 5 to 10 times for wide tables.  The method can now accept
  any input which convertible to a column of the correct length, not just
  ``Column`` subclasses.[#8902]

- Improved the implementation of ``Table.add_column()`` to provide a speed-up
  of 2 to 10 (or more) when adding a column to tables, with increasing benefit
  as the number of columns increases.  The method can now accept any input
  which is convertible to a column of the correct length, not just ``Column``
  subclasses. [#8933]

- Changed the implementation of ``Table.add_columns()`` to use the new
  ``Table.add_column()`` method.  In most cases the performance is similar
  or slightly faster to the previous implemenation. [#8933]

- ``MaskedColumn.data`` will now return a plain ``MaskedArray`` rather than
  the previous (unintended) ``masked_BaseColumn``. [#8855]

- Adding depth-wise stacking ``cstack()`` in higher level table operation.
  It help will in stacking table column depth-wise. [#8939]

- Allow adding a table column as a list of mixin-type objects, for instance
  ``t['q'] = [1 * u.m, 2 * u.m]``. [#9165]

astropy.tests
^^^^^^^^^^^^^

astropy.time
^^^^^^^^^^^^

- ``TimeDelta`` gained a ``to_value`` method, so that it becomes easier to
  use it wherever a ``Quantity`` with units of time could be used. [#8762]

- Made scalar ``Time`` and ``TimeDelta`` objects hashable based on JD, time
  scale, and location attributes. [#8912]

astropy.timeseries
^^^^^^^^^^^^^^^^^^

astropy.uncertainty
^^^^^^^^^^^^^^^^^^^

astropy.units
^^^^^^^^^^^^^

- Accept non-unit type annotations in @quantity_input. [#8984]

- For numpy 1.17 and later, the new ``__array_function__`` protocol is used to
  ensure that all top-level numpy functions interact properly with
  ``Quantity``, preserving units also in operations like ``np.concatenate``.
  [#8808]

astropy.utils
^^^^^^^^^^^^^

astropy.visualization
^^^^^^^^^^^^^^^^^^^^^

- Added a new ``time_support`` context manager/function for making it easy to
  plot and format ``Time`` objects in Matplotlib. [#8782]

- Added support for plotting any WCS compliant with the generalized (APE 14)
  WCS API with WCSAxes. [#8885, #9098]

- Improved display of information when inspecting ``WCSAxes.coords``. [#9098]

- Improved error checking for the ``slices=`` argument to ``WCSAxes``. [#9098]

astropy.wcs
^^^^^^^^^^^

- Updated wcslib to v6.4. [#9125]

- Improved the  ``SlicedLowLevelWCS`` class in ``astropy.wcs.wcsapi`` to avoid
  storing chains of nested ``SlicedLowLevelWCS`` objects when applying multiple
  slicing operations in turn. [#9210]

- Added a ``wcs_info_str`` function to ``astropy.wcs.wcsapi`` to show a summary
- Added a ``wcs_as_str`` function to ``astropy.wcs.wcsapi`` to show a summary
- Added a ``wcs_info_str`` function to ``astropy.wcs.wcsapi`` to show a summary
  of an APE-14-compliant WCS as a string. [#8546, #9207]
- Added two new optional attributes to the APE 14 low-level WCS: ``pixel_axis_names``
  and ``world_axis_names``. [#9156]

API Changes
-----------

astropy.config
^^^^^^^^^^^^^^

astropy.constants
^^^^^^^^^^^^^^^^^

- Deprecated ``set_enabled_constants`` context manager. Use
  ``astropy.physical_constants`` and ``astropy.astronomical_constants``.
  [#9025]

astropy.convolution
^^^^^^^^^^^^^^^^^^^

astropy.coordinates
^^^^^^^^^^^^^^^^^^^

- Removed the ``recommended_units`` attribute from Representations; it was
  deprecated since 3.0. [#8892]

astropy.cosmology
^^^^^^^^^^^^^^^^^

astropy.extern
^^^^^^^^^^^^^^

astropy.io.ascii
^^^^^^^^^^^^^^^^

- Masked column handling has changed, see ``astropy.table`` entry below. [#8789]

astropy.io.misc
^^^^^^^^^^^^^^^

- Masked column handling has changed, see ``astropy.table`` entry below. [#8789]

- Removed deprecated ``usecPickle`` kwarg from ``fnunpickle`` and
  ``fnpickle``. [#8890]

astropy.io.fits
^^^^^^^^^^^^^^^

- Masked column handling has changed, see ``astropy.table`` entry below. [#8789]

- ``io.fits.Header`` has been made safe for subclasses for copying and slicing.
  As a result of this change, the private subclass ``CompImageHeader`` now always
  should be passed an explicit ``image_header``. [#9229]

astropy.io.registry
^^^^^^^^^^^^^^^^^^^

astropy.io.votable
^^^^^^^^^^^^^^^^^^

- Changed ``pedantic`` argument to ``verify`` and change it to have three
  string-based options (``ignore``, ``warn``, and ``exception``) instead of just
  being a boolean. In addition, changed default to ``ignore``, which means
  that warnings will not be shown by default when loading VO tables. [#8715]

astropy.modeling
^^^^^^^^^^^^^^^^

- Eliminates support for compound classes (but not compound
  instances!) [#8769]

- Slicing compound models more restrictive. [#8769]

- Shape of parameters now includes n_models as dimension. [#8769]

- Parameter instances now hold values instead of models. [#8769]

- Compound model parameters now share instance and value with
  constituent models. [#8769]

- No longer possible to assign slices of parameter values to model
  parameters attribute (it is possible to replace it with a complete array). [#8769]

- Many private attributes and methods have changed (see documentation). [#8769]

- Added analytical King model (KingProjectedAnalytic1D) [#9084]

astropy.nddata
^^^^^^^^^^^^^^

astropy.samp
^^^^^^^^^^^^

astropy.stats
^^^^^^^^^^^^^

- Removed the ``iters`` keyword from sigma clipping stats functions.
  [#8948]

- Renamed the ``a`` parameter to ``data`` in biweight stat functions.
  [#8948]

- Renamed the ``a`` parameter to ``data`` in ``median_absolute_deviation``.
  [#9011]

astropy.table
^^^^^^^^^^^^^

- The handling of masked columns in the ``Table`` class has changed in a way
  that may impact program behavior. Now a ``Table`` with ``masked=False`` may
  contain both ``Column`` and ``MaskedColumn`` objects, and adding a masked
  column or row to a table no longer "upgrades" the table and columns to masked.
  This means that tables with masked data which are read via ``Table.read()``
  will now always have ``masked=False``, though specific columns will be masked as
  needed. Two new table properties ``has_masked_columns`` and ``has_masked_values``
  were added. See the ``Masking change in astropy 4.0`` section within
  `<https://docs.astropy.org/en/latest/table/masking.html>`_ for details. [#8789]

- Table operation functions such as ``join``, ``vstack``, ``hstack``, etc now
  always return a table with ``masked=False``, though the individual columns may
  be masked as necessary. [#8957]

- Changed implementation of ``Table.add_column()`` and ``Table.add_columns()``
  methods.  Now it is possible add any object(s) which can be converted or broadcasted
  to a valid column for the table.  ``Table.__setitem__`` now just calls
  ``add_column``.

- Changed default table configuration setting ``replace_warnings`` from
  ``['slice']`` to ``[]``.  This removes the default warning when replacing
  a table column that is a slice of another column. [#9144]

- Removed the non-public method ``astropy.table.np_utils.recarray_fromrecords``.
  [#9165]

astropy.tests
^^^^^^^^^^^^^

astropy.time
^^^^^^^^^^^^

- ``Time.get_ut1_utc`` now uses the auto-updated ``IERS_Auto`` by default,
  instead of the bundled ``IERS_B`` file. [#9226]

astropy.timeseries
^^^^^^^^^^^^^^^^^^

astropy.uncertainty
^^^^^^^^^^^^^^^^^^^

astropy.units
^^^^^^^^^^^^^

- For consistency with ``ndarray``, scalar ``Quantity.value`` will now return
  a numpy scalar rather than a python one.  This should help keep track of
  precision better, but may lead to unexpected results for the rare cases
  where numpy scalars behave differently than python ones (e.g., taking the
  square root of a negative number). [#8876]

astropy.utils
^^^^^^^^^^^^^

- Removed deprecated ``funcsigs`` and ``futures`` from
  ``astropy.utils.compat``. [#8909]

- Removed the deprecated ``astropy.utils.compat.numpy`` module. [#8910]

- Deprecated ``InheritDocstrings`` as it is natively supported by
  Sphinx 1.7 or higher. [#8881]

- Deprecated ``astropy.utils.timer`` module, which has been moved to
  ``astroquery.utils.timer`` and will be part of ``astroquery`` 0.4.0. [#9038]

- The implementation of ``data_info.DataInfo`` has changed (for a considerable
  performance boost). Generally, this should not affect simple subclasses, but
  because the class now uses ``__slots__`` any attributes on the class have to
  be explicitly given a slot. [#8998]

- ``IERS`` tables now use ``nan`` to mark missing values (rather than ``1e20``).
  [#9226]

astropy.visualization
^^^^^^^^^^^^^^^^^^^^^

astropy.wcs
^^^^^^^^^^^

Bug Fixes
---------

astropy.config
^^^^^^^^^^^^^^

astropy.constants
^^^^^^^^^^^^^^^^^

astropy.convolution
^^^^^^^^^^^^^^^^^^^

astropy.coordinates
^^^^^^^^^^^^^^^^^^^

astropy.cosmology
^^^^^^^^^^^^^^^^^

astropy.extern
^^^^^^^^^^^^^^

astropy.io.ascii
^^^^^^^^^^^^^^^^

astropy.io.misc
^^^^^^^^^^^^^^^

astropy.io.fits
^^^^^^^^^^^^^^^

astropy.io.registry
^^^^^^^^^^^^^^^^^^^

astropy.io.votable
^^^^^^^^^^^^^^^^^^

astropy.modeling
^^^^^^^^^^^^^^^^

astropy.nddata
^^^^^^^^^^^^^^

astropy.samp
^^^^^^^^^^^^

astropy.stats
^^^^^^^^^^^^^

astropy.table
^^^^^^^^^^^^^

- Fix bug where adding a column consisting of a list of masked arrays was
  dropping the masks. [#9048]

- ``Quantity`` columns with custom units can now round-trip via FITS tables,
  as long as the custom unit is enabled during reading (otherwise, the unit
  will become an ``UnrecognizedUnit``). [#9015]

astropy.tests
^^^^^^^^^^^^^

astropy.time
^^^^^^^^^^^^

astropy.timeseries
^^^^^^^^^^^^^^^^^^

astropy.uncertainty
^^^^^^^^^^^^^^^^^^^

astropy.units
^^^^^^^^^^^^^

astropy.utils
^^^^^^^^^^^^^

- For the default ``IERS_Auto`` table, which combines IERS A and B values, the
  IERS nutation parameters "dX_2000A" and "dY_2000A" are now also taken from
  the actual IERS B file rather than from the B values stored in the IERS A
  file.  Any differences should be negligible for any practical application,
  but this may help exactly reproducing results. [#9237]

astropy.visualization
^^^^^^^^^^^^^^^^^^^^^

astropy.wcs
^^^^^^^^^^^


Other Changes and Additions
---------------------------

- Versions of Python <3.6 are no longer supported. [#8955]

- Matplotlib 2.1 and later is now required. [#8787]

- Updated the bundled CFITSIO library to 3.470. See
  ``cextern/cfitsio/docs/changes.txt`` for additional information. [#9233]


3.2.2 (unreleased)
==================

Bug fixes
---------

astropy.config
^^^^^^^^^^^^^^

astropy.constants
^^^^^^^^^^^^^^^^^

astropy.convolution
^^^^^^^^^^^^^^^^^^^

astropy.coordinates
^^^^^^^^^^^^^^^^^^^

- Fix concatenation of representations for cases where the units were different.
  [#8877]

- Check for NaN values in catalog and match coordinates before building and
  querying the ``KDTree`` for coordinate matching. [#9007]
- Fix sky coordinate matching when a dimensionless distance is provided. [#9008]

astropy.cosmology
^^^^^^^^^^^^^^^^^

astropy.extern
^^^^^^^^^^^^^^

astropy.io.ascii
^^^^^^^^^^^^^^^^

- Fixed the fast reader when used in parallel and with the multiprocessing
  'spawn' method (which is the default on MacOS X with Python 3.8 and later),
  and enable parallel fast reader on Windows. [#8853]

astropy.io.misc
^^^^^^^^^^^^^^^

astropy.io.fits
^^^^^^^^^^^^^^^

- Fixes bug where an invalid TRPOS<n> keyword was being generated for FITS
  time column when no location was available. [#8784]

- Fixed a wrong exception when converting a Table with a unit that is not FITS
  compliant and not convertible to a string using ``format='fits'``. [#8906]

- Fixed an issue with A3DTABLE extension that could not be read. [#9012]

- Fixed the update of the header when creating GroupsHDU from data. [#9216]

astropy.io.registry
^^^^^^^^^^^^^^^^^^^

astropy.io.votable
^^^^^^^^^^^^^^^^^^

astropy.modeling
^^^^^^^^^^^^^^^^

Ensure unit information is properly applied to models evaluated with a
bounding box. [#8799]

astropy.nddata
^^^^^^^^^^^^^^

- Fix to ``add_array``, which now accepts ``array_small`` having dimensions
  equal to ``array_large``, instead of only allowing smaller sizes of
  arrays. [#9118]

astropy.samp
^^^^^^^^^^^^

astropy.stats
^^^^^^^^^^^^^

astropy.table
^^^^^^^^^^^^^

- Comparisons between ``Column`` instances and ``Quantity`` will now
  correctly take into account the unit (as was already the case for
  regular operations such as addition). [#8904]

astropy.tests
^^^^^^^^^^^^^

astropy.time
^^^^^^^^^^^^

- Allow ``Time`` to be initialized with an empty value for all formats. [#8854]

astropy.timeseries
^^^^^^^^^^^^^^^^^^

astropy.uncertainty
^^^^^^^^^^^^^^^^^^^

astropy.units
^^^^^^^^^^^^^

- Ensure that output from test functions of and comparisons between quantities
  can be stored into pre-allocated output arrays (using ``out=array``) [#9273]

astropy.utils
^^^^^^^^^^^^^

- Fixed ``find_api_page`` access by using custom request headers and HTTPS
  when version is specified. [#9032]

astropy.visualization
^^^^^^^^^^^^^^^^^^^^^

- Silence numpy runtime warnings in ``WCSAxes`` when drawing grids. [#8882]

astropy.wcs
^^^^^^^^^^^

- Fixed equality test between ``cunit`` where the first element was equal but
  the following elements differed. [#9154]

- Fixed a crash while loading a WCS from headers containing duplicate SIP keywords. [#8893]

- Fixed a possible buffer overflow when using too large negative indices for
  ``cunit`` or ``ctype`` [#9151]

- Fixed reference counting in ``WCSBase.__init__`` [#9166]


Other Changes and Additions
---------------------------

- Fixed a bug that caused files outside of the astropy module directory to be
  included as package data, resulting in some cases in errors when doing
  repeated builds. [#9039]


3.2.1 (2019-06-14)
==================

Bug fixes
---------

astropy.io.fits
^^^^^^^^^^^^^^^

- Avoid reporting a warning with ``BinTableHDU.from_columns`` with keywords that
  are not provided by the user.  [#8838]

- Fix ``Header.fromfile`` to work on FITS files. [#8713]

- Fix reading of empty ``BinTableHDU`` when stored in a gzip-compressed file.
  [#8848]

astropy.table
^^^^^^^^^^^^^

- Fix a problem where mask was dropped when creating a ``MaskedColumn``
  from a list of ``MaskedArray`` objects. [#8826]

astropy.wcs
^^^^^^^^^^^

- Added ``None`` to be displayed as a ``world_axis_physical_types`` in
  the ``WCS`` repr, as ``None`` values are now supported in ``APE14``. [#8811]



3.2 (2019-06-10)
================

New Features
------------

astropy.constants
^^^^^^^^^^^^^^^^^

- Add CODATA 2018 constants but not make them default because the
  redefinition of SI units that will follow has not been implemented
  yet. [#8595]

astropy.coordinates
^^^^^^^^^^^^^^^^^^^

- New ``BarycentricMeanEcliptic``, ``HeliocentricTrueEcliptic`` and
  ``GeocentricTrueEcliptic`` frames.
  The ecliptic frames are no longer considered experimental. [#8394]

- The default time scale for epochs like 'J2000' or 'B1975' is now "tt",
  which is the correct one for 'J2000' and avoids leap-second warnings
  for epochs in the far future or past. [#8600]

astropy.extern
^^^^^^^^^^^^^^

- Bundled ``six`` now emits ``AstropyDeprecationWarning``. It will be removed
  in 4.0. [#8323]

astropy.io.ascii
^^^^^^^^^^^^^^^^

- IPAC tables now output data types of ``float`` instead of ``double``, or
  ``int`` instead of ``long``, based on the column ``dtype.itemsize``. [#8216]

- Update handling of MaskedColumn columns when using the 'data_mask' serialization
  method.  This can make writing ECSV significantly faster if the data do not
  actually have any masked values. [#8447]

- Fixed a bug that caused newlines to be incorrect when writing out ASCII tables
  on Windows (they were ``\r\r\n`` instead of ``\r\n``). [#8659]

astropy.io.misc
^^^^^^^^^^^^^^^

- Implement serialization of ``TimeDelta`` in ASDF. [#8285]

- Implement serialization of ``EarthLocation`` in ASDF. [#8286]

- Implement serialization of ``SkyCoord`` in ASDF. [#8284]

- Support serialization of Astropy tables with mixin columns in ASDF. [#8337]

- No warnings when reading HDF5 files with only one table and no ``path=``
  argument [#8483]

- The HDF5 writer will now create a default table instead of raising an
  exception when ``path=`` is not specified and when writing to empty/new HDF5
  files. [#8553]

astropy.io.fits
^^^^^^^^^^^^^^^

- Optimize parsing of cards within the ``Header`` class. [#8428]

- Optimize the parsing of headers to get the structural keywords that are
  needed to find extensions. Thanks to this, getting a random HDU from a file
  with many extensions is much faster than before, in particular when the
  extension headers contain many keywords. [#8502]

-  Change behavior of FITS undefined value in ``Header`` such that ``None``
   is used in Python to represent FITS undefined when using dict interface.
   ``Undefined`` can also be assigned and is translated to ``None``.
   Previously setting a header card value to ``None`` resulted in an
   empty string field rather than a FITS undefined value. [#8572]

- Allow ``Header.fromstring`` and ``Card.fromstring`` to accept ``bytes``.
  [#8707]

astropy.io.registry
^^^^^^^^^^^^^^^^^^^

- Implement ``Table`` reader and writer for ``ASDF``. [#8261]

- Implement ``Table`` reader and writer methods to wrap ``pandas`` I/O methods
  for CSV, Fixed width format, HTML, and JSON. [#8381]

- Add ``help()`` and ``list_formats()`` methods to unified I/O ``read`` and
  ``write`` methods. For example ``Table.read.help()`` gives help on available
  ``Table`` read formats and ``Table.read.help('fits')`` gives detailed
  help on the arguments for reading FITS table file. [#8255]

astropy.table
^^^^^^^^^^^^^

- Initializing a table with ``Table(rows=...)``, if the first item is an ``OrderedDict``,
  now uses the column order of the first row. [#8587]

- Added new pprint_all() and pformat_all() methods to Table. These two new
  methods print the entire table by default. [#8577]

- Removed restriction of initializing a Table from a dict with copy=False. [#8541]

- Improved speed of table row access by a factor of about 2-3.  Improved speed
  of Table len() by a factor of around 3-10 (depending on the number of columns).
  [#8494]

- Improved the Table - pandas ``DataFrame`` interface (``to_pandas()`` and
  ``from_pandas()``).  Mixin columns like ``Time`` and ``Quantity`` can now be
  converted to pandas by flattening the columns as necessary to plain
  columns.  ``Time`` and ``TimeDelta`` columns get converted to
  corresponding pandas date or time delta types.  The ``DataFrame``
  index is now handled in the conversion methods. [#8247]

- Added ``rename_columns`` method to rename multiple columns in one call.
  [#5159, #8070]

- Improved Table performance by reducing unnecessary calls to copy and deepcopy,
  especially as related to the table and column ``meta`` attributes.  Changed the
  behavior when slicing a table (either in rows or with a list of column names)
  so now the sliced output gets a light (key-only) copy of ``meta`` instead of a
  deepcopy.  Changed the ``Table.meta`` class-level descriptor so that assigning
  directly to ``meta``, e.g. ``tbl.meta = new_meta`` no longer does a deepcopy
  and instead just directly assigns the ``new_meta`` object reference.  Changed
  Table initialization so that input ``meta`` is copied only if ``copy=True``.
  [#8404]

- Improved Table slicing performance with internal implementation changes
  related to column attribute access and certain input validation. [#8493]

- Added ``reverse`` argument to the ``sort`` and ``argsort`` methods to allow
  sorting in reverse order. [#8528]

- Improved ``Table.sort()`` performance by removing ``self[keys]`` from code
  which is creating deep copies of ``meta`` attribute and adding a new keyword
  ``names`` in ``get_index()`` to get index by using a list or tuple containing
  names of columns. [#8570]

- Expose ``represent_mixins_as_columns`` as a public function in the
  ``astropy.table`` subpackage.  This previously-private function in the
  ``table.serialize`` module is used to represent mixin columns in a Table as
  one or more plain Column objects. [#7729]

astropy.timeseries
^^^^^^^^^^^^^^^^^^

- Added a new astropy.timeseries sub-package to represent and manipulate
  sampled and binned time series. [#8540]

- The ``BoxLeastSquares`` and ``LombScargle`` classes have been moved to
  ``astropy.timeseries.periodograms`` from ``astropy.stats``. [#8591]

- Added the ability to provide absolute ``Time`` objects to the
  ``BoxLeastSquares`` and ``LombScargle`` periodogram classes. [#8599]

- Added model inspection methods (``model_parameters()``, ``design_matrix()``,
  and ``offset()``) to ``astropy.timeseries.LombScargle`` class [#8397].

astropy.units
^^^^^^^^^^^^^

- ``Quantity`` overrides of ``ndarray`` methods such as ``sum``, ``min``,
  ``max``, which are implemented via reductions, have been removed since they
  are dealt with in ``Quantity.__array_ufunc__``. This should not affect
  subclasses, but they may consider doing similarly. [#8316]  Note that this
  does not include methods that use more complicated python code such as
  ``mean``, ``std`` and ``var``. [#8370]

astropy.visualization
^^^^^^^^^^^^^^^^^^^^^
- Added ``CompositeStretch``, which inherits from ``CompositeTransform`` and
  also ``BaseStretch`` so that it can be used with ``ImageNormalize``. [#8564]

- Added a ``log_a`` argument to the ``simple_norm`` method. Similar to the
  exposing of the ``asinh_a`` argument for ``AsinhStretch``, the new
  ``log_a`` argument is now exposed for ``LogStretch``. [#8436]

astropy.wcs
^^^^^^^^^^^

- WCSLIB was updated to v 6.2.
  This adds support for time-related WCS keywords (WCS Paper VII).
  FITS headers containing ``Time`` axis are parsed and the axis is included in
  the WCS object. [#8592]

- The ``OBSGEO`` attribute as expanded to 6 members - ``XYZLBH``. [#8592]

- Added a new class ``SlicedLowLevelWCS`` in ``astropy.wcs.wcsapi`` that can be
  used to slice any WCS that conforms to the ``BaseLowLevelWCS`` API. [#8546]

- Updated implementation of ``WCS.__getitem__`` and ``WCS.slice`` to now return
  a ``SlicedLowLevelWCS`` rather than raising an error when reducing the
  dimensionality of the WCS. [#8546]


API Changes
-----------

astropy.coordinates
^^^^^^^^^^^^^^^^^^^

- ``QuantityAttribute`` no longer has a default value for ``default``.  The
  previous value of None was misleading as it always was an error. [#8450]

- The default J2000 has been changed to use be January 1, 2000 12:00 TT instead
  of UTC.  This is more in line with convention. [#8594]

astropy.io.ascii
^^^^^^^^^^^^^^^^

- IPAC tables now output data types of ``float`` instead of ``double``, or
  ``int`` instead of ``long``, based on the column ``dtype.itemsize``. [#8216]

astropy.io.misc
^^^^^^^^^^^^^^^

- Unit equivalencies can now be serialized to ASDF. [#8252]

astropy.modeling
^^^^^^^^^^^^^^^^

- Composition of model classes is deprecated and will be removed in 4.0.
  Composition of model instances remain unaffected. [#8234, #8408]

astropy.stats
^^^^^^^^^^^^^

- The ``BoxLeastSquares`` and ``LombScargle`` classes have been moved to the
  ``astropy.timeseries.periodograms`` module and will now emit a deprecation
  warning when imported from ``astropy.stats``. [#8591]

astropy.table
^^^^^^^^^^^^^

- Converting an empty table to an array using ``as_array`` method now returns
  an empty array instead of ``None``. [#8647]

- Changed the behavior when slicing a table (either in rows or with a list of column
  names) so now the sliced output gets a light (key-only) copy of ``meta`` instead of
  a deepcopy.  Changed the ``Table.meta`` class-level descriptor so that assigning
  directly to ``meta``, e.g. ``tbl.meta = new_meta`` no longer does a deepcopy
  and instead just directly assigns the ``new_meta`` object reference. Changed
  Table initialization so that input ``meta`` is copied only if ``copy=True``.
  [#8404]

- Added a keyword ``names`` in ``Table.as_array()``.  If provided this specifies
  a list of column names to include for the returned structured array. [#8532]

astropy.tests
^^^^^^^^^^^^^

- Removed ``pytest_plugins`` as they are completely broken for ``pytest>=4``.
  [#7786]

- Removed the ``astropy.tests.plugins.config`` plugin and removed the
  ``--astropy-config-dir`` and ``--astropy-cache-dir`` options from
  testing. Please use caching functionality that is natively in ``pytest``.
  [#7787, #8489]

astropy.time
^^^^^^^^^^^^

- The default time scale for epochs like 'J2000' or 'B1975' is now "tt",
  which is the correct one for 'J2000' and avoids leap-second warnings
  for epochs in the far future or past. [#8600]

astropy.units
^^^^^^^^^^^^^

- Unit equivalencies can now be introspected. [#8252]

astropy.wcs
^^^^^^^^^^^

- The ``world_to_pixel``, ``world_to_array_index*``, ``pixel_to_world*`` and
  ``array_index_to_world*`` methods now all consistently return scalars, arrays,
  or objects not wrapped in a one-element tuple/list when only one scalar,
  array, or object (as was previously already the case for ``WCS.pixel_to_world``
  and ``WCS.array_index_to_world``). [#8663]

astropy.utils
^^^^^^^^^^^^^

- It is now possible to control the number of cores used by ``ProgressBar.map``
  by passing a positive integer as the ``multiprocess`` keyword argument. Use
  ``True`` to use all cores. [#8083]


Bug Fixes
---------

astropy.coordinates
^^^^^^^^^^^^^^^^^^^

- ``BarycentricTrueEcliptic``, ``HeliocentricTrueEcliptic`` and
  ``GeocentricTrueEcliptic`` now use the correct transformation
  (including nutation), whereas the new ``*MeanEcliptic`` classes
  use the nutation-free transformation. [#8394]

- Representations with ``float32`` coordinates can now be transformed,
  although the output will always be ``float64``. [#8759]

- Fixed bug that prevented using differentials with HCRS<->ICRS
  transformations. [#8794]

astropy.io.ascii
^^^^^^^^^^^^^^^^

- Fixed a bug where an exception was raised when writing a table which includes
  mixin columns (e.g. a Quantity column) and the output format was specified
  using the ``formats`` keyword. [#8681]

astropy.io.misc
^^^^^^^^^^^^^^^

- Fixed bug in ASDF tag that inadvertently introduced dependency on ``pytest``.
  [#8456]

astropy.modeling
^^^^^^^^^^^^^^^^

- Fixed slowness for certain compound models consisting of large numbers
  of multi-input models [#8338, #8349]

- Fixed bugs in fitting of compound models with units. [#8369]

astropy.nddata
^^^^^^^^^^^^^^

- Fixed bug in reading multi-extension FITS files written by earlier versions
  of ``CCDData``. [#8534]

- Fixed two errors in the way ``CCDData`` handles FITS files with WCS in the
  header. Some of the WCS keywords that should have been removed from the
  header were not, potentially leading to FITS files with inconsistent
  WCS. [#8602]

astropy.table
^^^^^^^^^^^^^

- Fixed a bug when initializing from an empty list: ``Table([])`` no longer
  results in a crash. [#8647]

- Fixed a bug when initializing from an existing ``Table``.  In this case the
  input ``meta`` argument was being ignored.  Now the input ``meta``, if
  supplied, will be used as the ``meta`` for the new ``Table``. [#8404]

- Fix the conversion of bytes values to Python ``str`` with ``Table.tolist``.
  [#8739]

astropy.time
^^^^^^^^^^^^

- Fixed a number of issues to ensure a consistent output type resulting from
  multiplication or division involving a ``TimeDelta`` instance. The output is
  now always a ``TimeDelta`` if the result is a time unit (like u.s or u.d),
  otherwise it will be a ``Quantity``. [#8356]

- Multiplication between two ``TimeDelta`` instances is now possible, resulting
  in a ``Quantity`` with units of time squared (division already correctly
  resulted in a dimensionless ``Quantity``). [#8356]

- Like for comparisons, addition, and subtraction of ``Time`` instances with
  with non-time instances, multiplication and division of ``TimeDelta``
  instances with incompatible other instances no longer immediately raise an
  ``UnitsError`` or ``TypeError`` (depending on the other instance), but
  rather go through the regular Python mechanism of ``TimeDelta`` returning
  ``NotImplemented`` (which will lead to a regular ``TypeError`` unless the
  other instance can handle ``TimeDelta``). [#8356]

- Corrected small rounding errors that could cause the ``jd2`` values in
  ``Time`` to fall outside the range of -0.5 to 0.5. [#8763]

astropy.units
^^^^^^^^^^^^^

- Added a ``Quantity.to_string`` method to add flexibility to the string formatting
  of quantities. It produces unadorned or LaTeX strings, and accepts two different
  sets of delimiters in the latter case: ``inline`` and ``display``. [#8313]

- Ensure classes that mimic quantities by having a ``unit`` attribute and/or
  ``to`` and ``to_value`` methods can be properly used to initialize ``Quantity``
  or set ``Quantity`` instance items. [#8535]

- Add support for ``<<`` to create logarithmic units. [#8290]

- Add support for the ``clip`` ufunc, which in numpy 1.17 is used to implement
  ``np.clip``.  As part of that, remove the ``Quantity.clip`` method under
  numpy 1.17. [#8747]

- Fix parsing of numerical powers in FITS-compatible units. [#8251]

astropy.wcs
^^^^^^^^^^^

- Added a ``PyUnitListProxy_richcmp`` method in ``UnitListProxy`` class to enable
  ``WCS.wcs.cunit`` equality testing. It helps to check whether the two instances of
  ``WCS.wcs.cunit`` are equal or not by comparing the data members of
  ``UnitListProxy`` class [#8480]

- Fixed ``SlicedLowLevelWCS`` when ``array_shape`` is ``None``. [#8649]

- Do not attempt to delete repeated distortion keywords multiple times when
  loading distortions with ``_read_distortion_kw`` and
  ``_read_det2im_kw``. [#8777]


Other Changes and Additions
---------------------------

- Update bundled expat to 2.2.6. [#8343]

- Added instructions for uploading releases to Zenodo. [#8395]

- The bug fixes to the behaviour of ``TimeDelta`` for multiplcation and
  division, which ensure that the output is now always a ``TimeDelta`` if the
  result is a time unit (like u.s or u.d) and otherwise a ``Quantity``, imply
  that sometimes the output type will be different than it was before. [#8356]

- For types unrecognized by ``TimeDelta``, multiplication and division now
  will consistently return a ``TypeError`` if the other instance cannot handle
  ``TimeDelta`` (rather than ``UnitsError`` or ``TypeError`` depending on
  presumed abilities of the other instance). [#8356]

- Multiplication between two ``TimeDelta`` instances will no longer result in
  an ``OperandTypeError``, but rather result in a ``Quantity`` with units of
  time squared (division already correctly resulted in a dimensionless
  ``Quantity``). [#8356]

- Made running the tests insensitive to local user configuration when running
  the tests in parallel mode or directly with pytest. [#8727]

- Added a narrative style guide to the documentation for contributor reference.
  [#8588]

- Ensure we call numpy equality functions in a way that reduces the number
  of ``DeprecationWarning``. [#8755]

Installation
^^^^^^^^^^^^

- We now require setuptools 30.3.0 or later to install the core astropy
  package. [#8240]

- We now define groups of dependencies that can be installed with pip, e.g.
  ``pip install astropy[all]`` (to install all optional dependencies). [#8198]

0.2 (2013-02-19)
================

New Features
------------

astropy.coordinates
^^^^^^^^^^^^^^^^^^^

- This new subpackage contains a representation of celestial coordinates,
  and provides a wide range of related functionality.  While
  fully-functional, it is a work in progress and parts of the API may
  change in subsequent releases.

astropy.cosmology
^^^^^^^^^^^^^^^^^

- Update to include cosmologies with variable dark energy equations of state.
  (This introduces some API incompatibilities with the older Cosmology
  objects).

- Added parameters for relativistic species (photons, neutrinos) to the
  astropy.cosmology classes. The current treatment assumes that neutrinos are
  massless. [#365]

- Add a WMAP9 object using the final (9-year) WMAP parameters from
  Hinshaw et al. 2013. It has also been made the default cosmology.
  [#629, #724]

- astropy.table I/O infrastructure for custom readers/writers
  implemented. [#305]

- Added support for reading/writing HDF5 files [#461]

- Added support for masked tables with missing or invalid data [#451]

- New ``astropy.time`` sub-package. [#332]

- New ``astropy.units`` sub-package that includes a class for units
  (``astropy.units.Unit``) and scalar quantities that have units
  (``astropy.units.Quantity``). [#370, #445]

  This has the following effects on other sub-packages:

- In ``astropy.wcs``, the ``wcs.cunit`` list now takes and returns
  ``astropy.units.Unit`` objects. [#379]

- In ``astropy.nddata``, units are now stored as ``astropy.units.Unit``
  objects. [#382]

- In ``astropy.table``, units on columns are now stored as
  ``astropy.units.Unit`` objects. [#380]

- In ``astropy.constants``, constants are now stored as
  ``astropy.units.Quantity`` objects. [#529]

astropy.io.ascii
^^^^^^^^^^^^^^^^

- Improved integration with the ``astropy.table`` Table class so that
  table and column metadata (e.g. keywords, units, description,
  formatting) are directly available in the output table object.  The
  CDS, DAOphot, and IPAC format readers now provide this type of
  integrated metadata.

- Changed to using ``astropy.table`` masked tables instead of NumPy
  masked arrays for tables with missing values.

- Added SExtractor table reader to ``astropy.io.ascii`` [#420]

- Removed the Memory reader class which was used to convert data input
  passed to the ``write`` function into an internal table.  Instead
  ``write`` instantiates an astropy Table object using the data
  input to ``write``.

- Removed the NumpyOutputter as the output of reading a table is now
  always a ``Table`` object.

- Removed the option of supplying a function as a column output
  formatter.

- Added a new ``strip_whitespace`` keyword argument to the ``write``
  function.  This controls whether whitespace is stripped from
  the left and right sides of table elements before writing.
  Default is True.

- Fixed a bug in reading IPAC tables with null values.

- Generalized I/O infrastructure so that ``astropy.nddata`` can also have
  custom readers/writers [#659]

astropy.wcs
^^^^^^^^^^^

- From updating the underlying wcslib 4.16:

- When ``astropy.wcs.WCS`` constructs a default coordinate representation
  it will give it the special name "DEFAULTS", and will not report "Found
  one coordinate representation".

Other Changes and Additions
---------------------------

- A configuration file with all options set to their defaults is now generated
  when astropy is installed.  This file will be pulled in as the users'
  astropy configuration file the first time they ``import astropy``.  [#498]

- Astropy doc themes moved into ``astropy.sphinx`` to allow affiliated packages
  to access them.

- Added expanded documentation for the ``astropy.cosmology`` sub-package.
  [#272]

- Added option to disable building of "legacy" packages (pyfits, vo, etc.).

- The value of the astronomical unit (au) has been updated to that adopted by
  IAU 2012 Resolution B2, and the values of the pc and kpc constants have been
  updated to reflect this. [#368]

- Added links to the documentation pages to directly edit the documentation on
  GitHub. [#347]

- Several updates merged from ``pywcs`` into ``astropy.wcs`` [#384]:

- Improved the reading of distortion images.

- Added a new option to choose whether or not to write SIP coefficients.

- Uses the ``relax`` option by default so that non-standard keywords are
  allowed. [#585]


- Added HTML representation of tables in IPython notebook [#409]

- Rewrote CFITSIO-based backend for handling tile compression of FITS files.
  It now uses a standard CFITSIO instead of heavily modified pieces of CFITSIO
  as before.  Astropy ships with its own copy of CFITSIO v3.30, but system
  packagers may choose instead to strip this out in favor of a
  system-installed version of CFITSIO.  This corresponds to PyFITS ticket 169.
  [#318]

- Moved ``astropy.config.data`` to ``astropy.utils.data`` and re-factored the
  I/O routines to separate out the generic I/O code that can be used to open
  any file or resource from the code used to access Astropy-related data. The
  'core' I/O routine is now ``get_readable_fileobj``, which can be used to
  access any local as well as remote data, supports caching, and can decompress
  gzip and bzip2 files on-the-fly. [#425]

- Added a classmethod to
  ``astropy.coordinates.coordsystems.SphericalCoordinatesBase`` that performs a
  name resolve query using Sesame to retrieve coordinates for the requested
  object. This works for any subclass of ``SphericalCoordinatesBase``, but
  requires an internet connection. [#556]

- astropy.nddata.convolution removed requirement of PyFFTW3; uses Numpy's
  FFT by default instead with the added ability to specify an FFT
  implementation to use. [#660]


Bug Fixes
---------

astropy.io.ascii
^^^^^^^^^^^^^^^^

- Fixed crash when pprinting a row with INDEF values. [#511]

- Fixed failure when reading DAOphot files with empty keyword values. [#666]

astropy.io.fits
^^^^^^^^^^^^^^^

- Improved handling of scaled images and pseudo-unsigned integer images in
  compressed image HDUs.  They now work more transparently like normal image
  HDUs with support for the ``do_not_scale_image_data`` and ``uint`` options,
  as well as ``scale_back`` and ``save_backup``.  The ``.scale()`` method
  works better too. Corresponds to PyFITS ticket 88.

- Permits non-string values for the EXTNAME keyword when reading in a file,
  rather than throwing an exception due to the malformatting.  Added
  verification for the format of the EXTNAME keyword when writing.
  Corresponds to PyFITS ticket 96.

- Added support for EXTNAME and EXTVER in PRIMARY HDUs.  That is, if EXTNAME
  is specified in the header, it will also be reflected in the ``.name``
  attribute and in ``fits.info()``.  These keywords used to be verboten in
  PRIMARY HDUs, but the latest version of the FITS standard allows them.
  Corresponds to PyFITS ticket 151.

- HCOMPRESS can again be used to compress data cubes (and higher-dimensional
  arrays) so long as the tile size is effectively 2-dimensional. In fact,
  compatible tile sizes will automatically be used even if they're not
  explicitly specified. Corresponds to PyFITS ticket 171.

- Fixed a bug that could cause a deadlock in the filesystem on OSX when
  reading the data from certain types of FITS files. This only occurred
  when used in conjunction with Numpy 1.7. [#369]

- Added support for the optional ``endcard`` parameter in the
  ``Header.fromtextfile()`` and ``Header.totextfile()`` methods.  Although
  ``endcard=False`` was a reasonable default assumption, there are still text
  dumps of FITS headers that include the END card, so this should have been
  more flexible. Corresponds to PyFITS ticket 176.

- Fixed a crash when running fitsdiff on two empty (that is, zero row) tables.
  Corresponds to PyFITS ticket 178.

- Fixed an issue where opening a FITS file containing a random group HDU in
  update mode could result in an unnecessary rewriting of the file even if
  no changes were made. This corresponds to PyFITS ticket 179.

- Fixed a crash when generating diff reports from diffs using the
  ``ignore_comments`` options. Corresponds to PyFITS ticket 181.

- Fixed some bugs with WCS distortion paper record-valued keyword cards:

- Cards that looked kind of like RVKCs but were not intended to be were
  over-permissively treated as such--commentary keywords like COMMENT and
  HISTORY were particularly affected. Corresponds to PyFITS ticket 183.

- Looking up a card in a header by its standard FITS keyword only should
  always return the raw value of that card.  That way cards containing
  values that happen to valid RVKCs but were not intended to be will still
  be treated like normal cards. Corresponds to PyFITS ticket 184.

- Looking up a RVKC in a header with only part of the field-specifier (for
  example "DP1.AXIS" instead of "DP1.AXIS.1") was implicitly treated as a
  wildcard lookup. Corresponds to PyFITS ticket 184.

- Fixed a crash when diffing two FITS files where at least one contains a
  compressed image HDU which was not recognized as an image instead of a
  table. Corresponds to PyFITS ticket 187.

- Fixed a bug where opening a file containing compressed image HDUs in
  'update' mode and then immediately closing it without making any changes
  caused the file to be rewritten unnecessarily.

- Fixed two memory leaks that could occur when writing compressed image data,
  or in some cases when opening files containing compressed image HDUs in
  'update' mode.

- Fixed a bug where ``ImageHDU.scale(option='old')`` wasn't working at
  all--it was not restoring the image to its original BSCALE and BZERO
  values.

- Fixed a bug when writing out files containing zero-width table columns,
  where the TFIELDS keyword would be updated incorrectly, leaving the table
  largely unreadable.

- Fixed a minor string formatting issue.

- Fixed bugs in the backwards compatibility layer for the ``CardList.index``
  and ``CardList.count`` methods. Corresponds to PyFITS ticket 190.

- Improved ``__repr__`` and text file representation of cards with long
  values that are split into CONTINUE cards. Corresponds to PyFITS ticket
  193.

- Fixed a crash when trying to assign a long (> 72 character) value to blank
  ('') keywords. This also changed how blank keywords are represented--there
  are still exactly 8 spaces before any commentary content can begin; this
  *may* affect the exact display of header cards that assumed there could be
  fewer spaces in a blank keyword card before the content begins. However,
  the current approach is more in line with the requirements of the FITS
  standard. Corresponds to PyFITS ticket 194.

astropy.io.votable
^^^^^^^^^^^^^^^^^^

- The ``Table`` class now maintains a single array object which is a
  Numpy masked array.  For variable-length columns, the object that
  is stored there is also a Numpy masked array.

- Changed the ``pedantic`` configuration option to be ``False`` by default
  due to the vast proliferation of non-compliant VO Tables. [#296]

- Renamed ``astropy.io.vo`` to ``astropy.io.votable``.

astropy.table
^^^^^^^^^^^^^

- Added a workaround for an upstream bug in Numpy 1.6.2 that could cause
  a maximum recursion depth RuntimeError when printing table rows. [#341]

astropy.wcs
^^^^^^^^^^^

- Updated to wcslib 4.15 [#418]

- Fixed a problem with handling FITS headers on locales that do not use
  dot as a decimal separator. This required an upstream fix to wcslib which
  is included in wcslib 4.14. [#313]

- Fixed some tests that could fail due to missing/incorrect logging
  configuration--ensures that tests don't have any impact on the default log
  location or contents. [#291]

- Various minor documentation fixes [#293 and others]

- Fixed a bug where running the tests with the ``py.test`` command still tried
  to replace the system-installed pytest with the one bundled with Astropy.
  [#454]

- Improved multiprocessing compatibility for file downloads. [#615]

- Fixed handling of Cython modules when building from a source checkout of a
  tagged release version. [#594]

- Added a workaround for a bug in Sphinx that could occur when using the
  ``:tocdepth:`` directive. [#595]

- Minor VOTable fixes [#596]

- Fixed how ``setup.py`` uses ``distribute_setup.py`` to prevent possible
  ``VersionConflict`` errors when an older version of distribute is already
  installed on the user's system. [#616, #640]

- Changed use of ``log.warn`` in the logging module to ``log.warning`` since
  the former is deprecated. [#624]


0.1 (2012-06-19)
================

- Initial release.
