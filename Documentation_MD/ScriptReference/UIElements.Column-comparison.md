[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [Column](UIElements.Column.html).comparison

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

public Comparison<int> comparison;

### Description

The comparison to use when using
[ColumnSortingMode.Default](UIElements.ColumnSortingMode.Default.html).
Compares two items by their index in the source.

The following example creates a
[MultiColumnListView](UIElements.MultiColumnListView.html) that can be sorted
with the default algorithm:

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using System.IO;
    using System.Text;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.UIElements;
    using [Debug](Debug.html) = UnityEngine.Debug;  
      
    namespace MultiColumnViewExample
    {
        public class FileExplorerWindow : [EditorWindow](EditorWindow.html)
        {
            [MultiColumnListView](UIElements.MultiColumnListView.html) m_ListView;
            List<FileInfoWrapper> m_Source = new List<FileInfoWrapper>();
            StringBuilder m_StringBuilder = new StringBuilder();  
      
            [[MenuItem](MenuItem.html)("MultiColumnView Examples/[File](Windows.File.html) Explorer (List)")]
            public static void ShowExample()
            {
                var wnd = GetWindow<FileExplorerWindow>();
                wnd.titleContent = new [GUIContent](GUIContent.html)("[File](Windows.File.html) Explorer");
            }  
      
            public void CreateGUI()
            {
                // Here we're setting up a 3-column list view to display information on all files in the project.
                // Each column will be sorted using the `comparison` callback.
                // Use CTRL/CMD + click on a column header to sort multiple columns.
                // Use Shift + click on a column header to remove sorting.
                m_ListView = new [MultiColumnListView](UIElements.MultiColumnListView.html)(new [Columns](UIElements.Columns.html)()
                {
                    new [Column](UIElements.Column.html)()
                    {
                        name = "filename", title = "Name", minWidth = 600,
                        bindCell = (ve, row) => (([Label](UIElements.Label.html))ve).text = m_Source[row].fullFileName,
                        comparison = (a, b) => m_Source[a].fullFileName.CompareTo(m_Source[b].fullFileName),
                    },
                    new [Column](UIElements.Column.html)()
                    {
                        name = "type", title = "Type", minWidth = 60,
                        bindCell = (ve, row) => (([Label](UIElements.Label.html))ve).text = m_Source[row].type,
                        comparison = (a, b) => m_Source[a].type.CompareTo(m_Source[b].type),
                    },
                    new [Column](UIElements.Column.html)()
                    {
                        name = "size", title = "Size", minWidth = 60,
                        bindCell = (ve, row) => (([Label](UIElements.Label.html))ve).text = m_Source[row].displaySize,
                        comparison = (a, b) => m_Source[a].sizeLong.CompareTo(m_Source[b].sizeLong),
                    }
                });  
      
                // This causes the list view to take all the space available.
                m_ListView.style.flexGrow = 1;  
      
                // Setting the sortingMode to Default enables Unity's sorting algorithm, which will use the [Columns](UIElements.Columns.html)' comparison callbacks.
                m_ListView.sortingMode = [ColumnSortingMode.Default](UIElements.ColumnSortingMode.Default.html);  
      
                // Use all the files in the project as the source.
                foreach (var file in Directory.EnumerateFiles([Application.dataPath](Application-dataPath.html), "*.*", SearchOption.AllDirectories))
                {
                    m_Source.Add(new FileInfoWrapper(new FileInfo(file)));
                }  
      
                m_ListView.itemsSource = m_Source;  
      
                // The columnSortingChanged and sortedColumns property can be used to know when the ordering changes.
                // This is the callback to use if you want to implement a custom sorting algorithm, when using [ColumnSortingMode.Custom](UIElements.ColumnSortingMode.Custom.html).
                m_ListView.columnSortingChanged += () =>
                {
                    m_StringBuilder.Clear();
                    foreach (var s in m_ListView.sortedColumns)
                    {
                        m_StringBuilder.Append($"Sorted {s.columnName} in {s.direction} order.");
                    }  
      
                    [Debug.Log](Debug.Log.html)(m_StringBuilder.ToString());
                };  
      
                rootVisualElement.Add(m_ListView);
            }
        }  
      
        public class FileInfoWrapper
        {
            static readonly string[] k_SizeSuffixes = { "B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB" };  
      
            static string GetBytesReadable(long fileSizeInBytes)
            {
                if (fileSizeInBytes == 0)
                    return "0" + k_SizeSuffixes[0];  
      
                var magnitude = (int)Math.Log(fileSizeInBytes, 1024);
                var adjustedSize = fileSizeInBytes / (1L << (magnitude * 10));  
      
                return $"{adjustedSize:n1} {k_SizeSuffixes[magnitude]}";
            }  
      
            public FileInfoWrapper(FileInfo fileInfo)
            {
                fullFileName = fileInfo.FullName;
                type = fileInfo.Extension.Substring(1).ToUpper();
                displaySize = GetBytesReadable(fileInfo.Length);
                sizeLong = fileInfo.Length;
            }  
      
            public readonly string fullFileName;
            public readonly string type;
            public readonly string displaySize;
            public readonly long sizeLong; // It is faster to compare long than strings.
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

