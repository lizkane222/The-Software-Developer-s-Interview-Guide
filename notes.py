<ul id="dropdown-terms" class="dropdown-content">
        <li>
            <a href="cards/">All Terms</a>
        </li>
        <li class="divider"></li>
        {% for card in cards %}
        <li><a href="">{{card.term}}</a></li>
        {% endfor %}
    </ul>

    <ul id="dropdown-categories" class="dropdown-content">
        <li>
            <a href="/tree">All Languages</a>
        </li>
        <li class="divider"></li>
        {% for language in languages %}
        <li><a href="">{{language.name}}</a></li>
        {% endfor %}
    </ul>





RULES FOR NEW ELEMENTS:

Images are divs so they are inherently the parent div and the image is the child