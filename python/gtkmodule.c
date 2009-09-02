/*
 * Copyright (c) 2009 Mark Lee <libdesktop-agnostic@lazymalevolence.com>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the
 * Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
*/

#ifdef HAVE_BUILD_CONFIG_H
#include "build-config.h"
#endif

#include <pygobject.h>

/* the following symbols are declared in gtk.c: */
void pydesktopagnostic_gtk_register_classes (PyObject *d);
extern PyMethodDef pydesktopagnostic_gtk_functions[];

DL_EXPORT (void)
initgtk (void)
{
  PyObject *m, *d;

  init_pygobject ();

  m = Py_InitModule ("desktopagnostic.gtk", pydesktopagnostic_gtk_functions);
  d = PyModule_GetDict (m);

  pydesktopagnostic_gtk_register_classes (d);

  if (PyErr_Occurred ())
  {
    Py_FatalError ("Unable to initialise the desktopagnostic.gtk module");
  }
}
