from odoo import http, fields
from odoo.http import request

from odoo.addons.web.controllers.main import Home


class Home(Home):
    @http.route('/web/login', type='http', auth="public")
    def web_login(self, redirect=None, **kw):
        return super(Home, self).web_login(redirect, **kw)


class KartalHukuk(http.Controller):


    @http.route('/contactus', type='http', auth="public", website=True)
    def return_homepage(self):
        print("skdaşsldşals")
        return request.redirect('/Iletisim')

    @http.route('/Anasayfa', type="http", website=True, auth='public')
    def home(self, **kw):
        activities = request.env['kh.faaliyet'].sudo().search([])
        personnel = request.env['kh.avukat'].sudo().search([])
        return request.render("web_kartal_hukuk.home_page", {
            'activities': activities,
            'personnel': personnel
        })

    @http.route('/Hakkımızda', type="http", website=True, auth='public')
    def about(self, **kw):
        activities = request.env['kh.faaliyet'].sudo().search([])
        personnel = request.env['kh.avukat'].sudo().search([])
        return request.render("web_kartal_hukuk.about_page", {

            'activities': activities,
            'personnel': personnel
        })

    @http.route('/Kadromuz', type="http", website=True, auth='public')
    def team(self, **kw):
        activities = request.env['kh.faaliyet'].sudo().search([])
        personnel = request.env['kh.avukat'].sudo().search([])
        return request.render("web_kartal_hukuk.team_page", {
            'activities': activities,
            'personnel': personnel
        })

    @http.route('/Kadromuz/<string:ad>', type="http", website=True, auth='public')
    def team_detail(self, ad, **kw):
        activities = request.env['kh.faaliyet'].sudo().search([])
        personnel = request.env['kh.avukat'].sudo().search([('ad', '=', ad)])
        return request.render("web_kartal_hukuk.team_page_details", {
            'activities': activities,
            'personnel': personnel
        })

    @http.route('/Faaliyet-Alanları', type="http", website=True, auth='public')
    def activities(self, **kw):
        activities = request.env['kh.faaliyet'].sudo().search([])
        personnel = request.env['kh.avukat'].sudo().search([])
        return request.render("web_kartal_hukuk.activities_page", {
            'activities': activities,
            'personnel': personnel
        })

    @http.route('/Faaliyet-Alanları/<string:id>', type="http", website=True, auth='public')
    def activities_detail(self, id, **kw):
        activity = request.env['kh.faaliyet'].sudo().search([('id', '=', id)])
        personnel = request.env['kh.avukat'].sudo().search([])
        return request.render("web_kartal_hukuk.activities_page_details", {
            'activities': activity,
            'personnel': personnel
        })

    @http.route('/Vekalet-Bilgileri', type="http", website=True, auth='public')
    def deputation(self, **kw):
        activities = request.env['kh.faaliyet'].sudo().search([])
        personnel = request.env['kh.avukat'].sudo().search([])
        return request.render("web_kartal_hukuk.deputation_page", {
            'activities': activities,
            'personnel': personnel
        })

    @http.route(['/Güncel-Bilgiler', '/Güncel-Bilgiler/page/<int:page>'], type="http", website=True, auth='public')
    def article(self, page=1, search='', **kw):
        activities = request.env['kh.faaliyet'].sudo().search([])
        personnel = request.env['kh.avukat'].sudo().search([])

        domain = []
        url_args = {}

        if search:
            domain.append(('title', 'ilike', search))
            url_args['search'] = search

        articles = request.env['kh.article'].sudo().search(domain, offset=(page - 1) * 5, limit=5)
        total = articles.search_count([])

        url = '/Güncel-Bilgiler'
        pager = request.website.pager(url=url,
                                      total=total,
                                      page=page,
                                      step=5,
                                      url_args=url_args
                                      )

        return request.render("web_kartal_hukuk.article_page", {
            'activities': activities,
            'personnel': personnel,
            'search': search,
            'articles': articles,
            'pager': pager,


        })
    @http.route('/Güncel-Bilgiler/<string:id>', type="http", website=True, auth='public')
    def article_detail(self, id, **kw):
        articles = request.env['kh.article'].sudo().search([('id', '=', id)])
        activity = request.env['kh.faaliyet'].sudo().search([])
        personnel = request.env['kh.avukat'].sudo().search([])


        return request.render("web_kartal_hukuk.article_page_detail", {
            'activities': activity,
            'personnel': personnel,
            'article':articles
        })

    @http.route('/Faydalı-Linkler', type="http", website=True, auth='public')
    def links(self, **kw):
        activities = request.env['kh.faaliyet'].sudo().search([])
        personnel = request.env['kh.avukat'].sudo().search([])
        return request.render("web_kartal_hukuk.links_page", {
            'activities': activities,
            'personnel': personnel
        })

    @http.route('/Iletisim', type="http", website=True, auth='public')
    def contact(self, **kw):
        activities = request.env['kh.faaliyet'].sudo().search([])
        personnel = request.env['kh.avukat'].sudo().search([])
        return request.render("web_kartal_hukuk.contact_page", {
            'activities': activities,
            'personnel': personnel
        })

    @http.route('/CreateRequest', type="http", website=True, auth='public', methods=['POST'])
    def create_request(self, **kw):
        vals = {
            'name': kw.get('name'),
            'surname': kw.get('surname'),
            'phone': kw.get('phone'),
            'mail': kw.get('mail'),
            'comment': kw.get('comment'),
            'date': fields.Date.today()
        }

        request.env['kh.contact'].sudo().create(vals)
        last_id = request.env['kh.contact'].sudo().search([])[-1].id
        template_id = request.env.ref('web_kartal_hukuk.email_template').id
        template = request.env['mail.template'].sudo().browse(template_id)
        template.send_mail(last_id, force_send=True)
        return request.redirect('/Anasayfa')
