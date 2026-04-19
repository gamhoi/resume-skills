import sys
import json
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib import colors

def generate_pdf(json_path, output_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Heading1'],
        fontName='Times-Bold',
        fontSize=18,
        alignment=TA_CENTER,
        spaceAfter=3
    )
    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10,
        alignment=TA_CENTER,
        spaceAfter=12
    )
    heading_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Heading2'],
        fontName='Times-Bold',
        fontSize=14,
        textColor=colors.HexColor('#333333'),
        spaceBefore=8,
        spaceAfter=2,
        textTransform='uppercase'
    )
    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10,
        spaceAfter=3,
        leading=13
    )
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10,
        spaceAfter=2,
        leading=13,
        leftIndent=15,
        bulletIndent=5
    )

    story = []

    # 1. Header (Name & Contact)
    contact = data.get('contact', {})
    name = contact.get('name', 'Name Not Provided')
    story.append(Paragraph(name, name_style))

    contact_parts = []
    if contact.get('phone'): contact_parts.append(contact['phone'])
    if contact.get('email'): contact_parts.append(contact['email'])
    if contact.get('linkedin'): contact_parts.append(contact['linkedin'])
    if contact.get('location'): contact_parts.append(contact['location'])
    
    contact_text = " | ".join(contact_parts)
    story.append(Paragraph(contact_text, contact_style))

    # HR
    def add_hr():
        story.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.black, spaceBefore=2, spaceAfter=4))
    
    # 2. Summary
    if data.get('summary'):
        story.append(Paragraph("SUMMARY", heading_style))
        add_hr()
        if isinstance(data['summary'], list):
            for bullet in data['summary']:
                story.append(Paragraph(f"&bull; {bullet}", bullet_style))
        else:
            story.append(Paragraph(data['summary'], body_style))

    # 3. Work Experience
    if data.get('experience'):
        story.append(Paragraph("WORK EXPERIENCE", heading_style))
        add_hr()
        for job in data['experience']:
            # Job Header: Title (bold), Dates (right align)
            title = job.get('title', '')
            company = job.get('company', '')
            dates = job.get('dates', '')
            location = job.get('location', '')
            
            line1_left = f"<b>{title}</b>"
            line1_right = dates
            
            line2_left = f"<i>{company}</i>" + (f" - {location}" if location else "")
            
            # Using table for left/right alignment
            t_data = [
                [Paragraph(line1_left, body_style), Paragraph(line1_right, ParagraphStyle('R', parent=body_style, alignment=TA_RIGHT))],
                [Paragraph(line2_left, body_style), ""]
            ]
            t = Table(t_data, colWidths=['70%', '30%'])
            t.setStyle(TableStyle([
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('LEFTPADDING', (0,0), (-1,-1), 0),
                ('RIGHTPADDING', (0,0), (-1,-1), 0),
                ('BOTTOMPADDING', (0,0), (-1,-1), 0),
                ('TOPPADDING', (0,0), (-1,-1), 0),
            ]))
            story.append(t)
            story.append(Spacer(1, 4))
            
            for bullet in job.get('bullets', []):
                story.append(Paragraph(f"&bull; {bullet}", bullet_style))
            story.append(Spacer(1, 6))

    # 3.5. Other Professional Experience (optional)
    if data.get('other_experience'):
        story.append(Paragraph("OTHER PROFESSIONAL EXPERIENCE", heading_style))
        add_hr()
        for job in data['other_experience']:
            title = job.get('title', '')
            company = job.get('company', '')
            dates = job.get('dates', '')
            location = job.get('location', '')
            
            line1_left = f"<b>{title}</b>"
            line1_right = dates
            
            line2_left = f"<i>{company}</i>" + (f" - {location}" if location else "")
            
            t_data = [
                [Paragraph(line1_left, body_style), Paragraph(line1_right, ParagraphStyle('R', parent=body_style, alignment=TA_RIGHT))],
                [Paragraph(line2_left, body_style), ""]
            ]
            t = Table(t_data, colWidths=['70%', '30%'])
            t.setStyle(TableStyle([
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('LEFTPADDING', (0,0), (-1,-1), 0),
                ('RIGHTPADDING', (0,0), (-1,-1), 0),
                ('BOTTOMPADDING', (0,0), (-1,-1), 0),
                ('TOPPADDING', (0,0), (-1,-1), 0),
            ]))
            story.append(t)
            story.append(Spacer(1, 4))
            
            for bullet in job.get('bullets', []):
                story.append(Paragraph(f"&bull; {bullet}", bullet_style))
            story.append(Spacer(1, 6))

    # 3.6. Projects (optional)
    if data.get('projects'):
        story.append(Paragraph("PROJECTS", heading_style))
        add_hr()
        for proj in data['projects']:
            name = proj.get('name', '')
            dates = proj.get('dates', '')
            description = proj.get('description', '')
            
            line1_left = f"<b>{name}</b>"
            
            t_data = [
                [Paragraph(line1_left, body_style), Paragraph(dates, ParagraphStyle('R', parent=body_style, alignment=TA_RIGHT))]
            ]
            t = Table(t_data, colWidths=['70%', '30%'])
            t.setStyle(TableStyle([
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('LEFTPADDING', (0,0), (-1,-1), 0),
                ('RIGHTPADDING', (0,0), (-1,-1), 0),
                ('BOTTOMPADDING', (0,0), (-1,-1), 0),
                ('TOPPADDING', (0,0), (-1,-1), 0),
            ]))
            story.append(t)
            story.append(Spacer(1, 4))
            
            if description:
                story.append(Paragraph(description, body_style))
            
            for bullet in proj.get('bullets', []):
                story.append(Paragraph(f"&bull; {bullet}", bullet_style))
            story.append(Spacer(1, 6))

    # 4. Education
    if data.get('education'):
        story.append(Paragraph("EDUCATION", heading_style))
        add_hr()
        for edu in data['education']:
            degree = edu.get('degree', '')
            school = edu.get('school', '')
            dates = edu.get('dates', '')
            location = edu.get('location', '')
            
            line1_left = f"<b>{degree}</b>"
            line1_right = dates
            line2_left = f"{school}" + (f" - {location}" if location else "")
            
            t_data = [
                [Paragraph(line1_left, body_style), Paragraph(line1_right, ParagraphStyle('R', parent=body_style, alignment=TA_RIGHT))],
                [Paragraph(line2_left, body_style), ""]
            ]
            t = Table(t_data, colWidths=['70%', '30%'])
            t.setStyle(TableStyle([
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('LEFTPADDING', (0,0), (-1,-1), 0),
                ('RIGHTPADDING', (0,0), (-1,-1), 0),
                ('BOTTOMPADDING', (0,0), (-1,-1), 0),
                ('TOPPADDING', (0,0), (-1,-1), 0),
            ]))
            story.append(t)
            
            for detail in edu.get('details', []):
                story.append(Paragraph(detail, body_style))
            story.append(Spacer(1, 6))

    # 4.5 Certifications
    if data.get('certifications'):
        story.append(Paragraph("CERTIFICATIONS", heading_style))
        add_hr()
        for cert in data['certifications']:
            name = cert.get('name', '')
            date = cert.get('date', '')
            issuer = cert.get('issuer', '')
            
            line1_left = f"<b>{name}</b>"
            line1_right = date
            line2_left = issuer
            
            t_data = [
                [Paragraph(line1_left, body_style), Paragraph(line1_right, ParagraphStyle('R', parent=body_style, alignment=TA_RIGHT))],
                [Paragraph(line2_left, body_style), ""]
            ]
            t = Table(t_data, colWidths=['70%', '30%'])
            t.setStyle(TableStyle([
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('LEFTPADDING', (0,0), (-1,-1), 0),
                ('RIGHTPADDING', (0,0), (-1,-1), 0),
                ('BOTTOMPADDING', (0,0), (-1,-1), 0),
                ('TOPPADDING', (0,0), (-1,-1), 0),
            ]))
            story.append(t)
            story.append(Spacer(1, 4))
            story.append(Spacer(1, 6))

    # 5. Skills
    if data.get('skills'):
        story.append(Paragraph("SKILLS", heading_style))
        add_hr()
        for skill_cat in data['skills']:
            category = skill_cat.get('category', '')
            items = ", ".join(skill_cat.get('items', []))
            if category and items:
                story.append(Paragraph(f"<b>{category}:</b> {items}", body_style))
            elif items:
                story.append(Paragraph(items, body_style))
        story.append(Spacer(1, 6))

    doc.build(story)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python generate_resume.py <input.json> <output.pdf>")
        sys.exit(1)
    generate_pdf(sys.argv[1], sys.argv[2])
