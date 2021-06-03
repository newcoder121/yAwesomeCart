{% extends 'shop/basic.html' %}
{% block title%} My Awesome Cart Tracker{% endblock %}
{% block body %}
<div class="container">
    {{response}}
    <div class="col my-4">

        <h2>Payment status regarding your order Id {{response.ORDERID}}</h2>
        {% if response.RESPCODE == '01' %}
        ORDER SUCCESS
        {% else %}
        ORDER FAILURE
        {% endif%}

    </div>

</div>
{% endblock %}
{% block js %}
<script>
</script>
{% endblock %}
