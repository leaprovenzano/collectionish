{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

{% if objtype == 'class' %}
.. autoclass:: {{ objname }}

   {% block methods %}

   {% if methods %}
   **Methods**:


   {% for method in methods %}
    .. automethod:: {{ method }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block attributes %}
   {% if attributes %}
   .. rubric:: Attributes:
   .. autosummary::
   {% for item in attributes %}
      ~{{ name }}.{{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}
{% endif %}

{% if objtype == 'module' %}

.. automodule:: {{ fullname }}
    :members:

{% endif %}
