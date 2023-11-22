import { Component, OnInit } from '@angular/core';
import { Issue } from '../issue';
import { IssuesService } from '../issues.service';


@Component({
  selector: 'app-issue-list',
  templateUrl: './issue-list.component.html',
  styleUrls: ['./issue-list.component.css']
})
export class IssueListComponent implements OnInit {
  issues: Issue[] = [];
  showReportIssue = false;

  constructor(private issueService: IssuesService) { }


  // in order to get all the pending issues upon component initializing, we call ngOnInit
  ngOnInit(): void { 
    this.getIssues();
  }

  private getIssues() {
    this.issues = this.issueService.getPendingIssues();
  }

  onCloseReport() {
    this.showReportIssue = false;
    this.getIssues();
  }

  selectedIssue: Issue | null = null;
  onConfirm(confirmed: boolean) {
    if (confirmed && this.selectedIssue) {
    this.issueService.completeIssue(this.selectedIssue);
    this.getIssues();
    }
    this.selectedIssue = null;
  }

}
