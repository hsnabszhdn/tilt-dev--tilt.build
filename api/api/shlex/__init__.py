### AUTO-GENERATED ###
# This file was auto-generated by 'tilt dump api-docs' as part of a Tilt release.
# To make changes, modify the following file in the Tilt repository:
#   internal/tiltfile/api/shlex/__init__.py
# Generated by Tilt version v0.30.9, built 2022-10-08
### AUTO-GENERATED ###

def quote(s: str) -> str:
  """
  Returns a shell-escaped version of ``s``, which can be safely interpolated as
  a single token in a shell command.

  e.g.:

  .. code-block:: python

    mystring = "foo's bar"

    # bad - runs: `docker run -e foo=foo's bar myimage` (invalid shell - unmatched ')
    local('docker run -e foo=%s myimage' % mystring)

    # good - runs: `docker run -e foo='foo'"'"'s bar' myimage`
    #        which correctly sets $foo to "foo's bar"
    local('docker run -e foo=%s myimage' % shlex.quote(mystring))
  """
  pass
