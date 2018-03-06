﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
namespace Client
{
    public partial class UserTab : UserControl
    {
        ClientSocket cSock;
        private string projects;
        private string username;
        public UserTab()
        {
            InitializeComponent();
            foreach (Control Item in this.Controls)
        }

        public string Get_Latest()

        public void Set_Tab(ClientSocket cliSock, string projects, string username)
        {
            projectList.Items.Clear();
            versionList.Items.Clear();
            this.username = username;
            this.cSock = cliSock;
            this.projects = projects;
            this.projects = this.Fix_Format(this.projects);
        }

        public string Fix_Format(string project)

        public void Set_Table()

        private void projectList_SelectedIndexChanged(object sender, EventArgs e)
        {
            try
        }

        private void downloadBtn_Click(object sender, EventArgs e)
        {
            DialogResult result = folderBrowserDialogU.ShowDialog();
            if (result == DialogResult.OK && versionList.SelectedIndex > -1)
            {
                string path = folderBrowserDialogU.SelectedPath;
                string data = this.cSock.Download_Project(projectList.SelectedItem.ToString(), versionList.SelectedItem.ToString());
                string content = data.Split(new[] { "`~`" }, StringSplitOptions.None)[0];
                string extension = data.Split(new[] { "`~`" }, StringSplitOptions.None)[1];
                extension = extension.Replace("\0", string.Empty);
                if (extension != "png")
                {
                    StreamWriter NewFile = new StreamWriter(filePath);
                    NewFile.Write(content);
                    NewFile.Close();
                }
                else
                {
                    string filePath = path.Replace("\0", string.Empty) + "\\" + projectList.SelectedItem.ToString().Replace("\0", string.Empty) + "_" + versionList.SelectedItem.ToString().Replace(".", "_").Replace(" ", "").Replace("\0", string.Empty) + "." + extension.Replace("\0", string.Empty);
                    System.IO.File.WriteAllBytes(filePath, Convert.FromBase64String(content));
                }
            }
        }
    }
}
