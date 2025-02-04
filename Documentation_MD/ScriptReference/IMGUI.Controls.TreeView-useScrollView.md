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

#  [TreeView](IMGUI.Controls.TreeView.html).useScrollView

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

protected bool useScrollView;

### Description

When drawing the TreeView contents, will it be enclosed within a ScrollView?

When enabled, the contents of the TreeView is culled so that anything outside
of the ScrollView is not drawn. If the TreeView is contained within an
external ScrollView, such as the Inspector window, then disabling this allows
the TreeView to use the external ScrollView to perform its culling.

    
    
    using UnityEngine;  
      
    public class ExampleBehaviourScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // This is our example list.
        public string[] exampleList;
    }
    

To use the following script, add it to the Editor directory.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.IMGUI.Controls;
    using UnityEngine;  
      
    // Simple [TreeView](IMGUI.Controls.TreeView.html) that draws a single list property.
    class NewBehaviourScriptEditorTreeView : [TreeView](IMGUI.Controls.TreeView.html)
    {
        [SerializedProperty](SerializedProperty.html) m_Property;  
      
        public NewBehaviourScriptEditorTreeView([SerializedProperty](SerializedProperty.html) property) :
            base(new [TreeViewState](IMGUI.Controls.TreeViewState.html)())
        {
            m_Property = property;
            showBorder = true;
            showAlternatingRowBackgrounds = true;
            useScrollView = false; // We are using the Inspector [ScrollView](UIElements.ScrollView.html)  
      
            MultiColumnHeaderState.Column[] columns = new MultiColumnHeaderState.Column[2];
            for (int i = 0; i < columns.Length; ++i)
            {
                columns[i] = new MultiColumnHeaderState.Column();
                columns[i].minWidth = 50;
                columns[i].width = 100;
                columns[i].headerTextAlignment = [TextAlignment.Center](TextAlignment.Center.html);
                columns[i].canSort = false;
            }
            columns[0].headerContent = new [GUIContent](GUIContent.html)("Index");
            columns[1].headerContent = new [GUIContent](GUIContent.html)("Value");
            var multiColState = new [MultiColumnHeaderState](IMGUI.Controls.MultiColumnHeaderState.html)(columns);
            multiColumnHeader = new [MultiColumnHeader](IMGUI.Controls.MultiColumnHeader.html)(multiColState);
            multiColumnHeader.ResizeToFit();
            Reload();
        }  
      
        protected override [TreeViewItem](IMGUI.Controls.TreeViewItem.html) BuildRoot()
        {
            int arraySize = m_Property.arraySize;  
      
            var root = new [TreeViewItem](IMGUI.Controls.TreeViewItem.html) { id = -1, depth = -1, displayName = "Root" };
            var allItems = new List<[TreeViewItem](IMGUI.Controls.TreeViewItem.html)>(arraySize);
            for (int i = 0; i < arraySize; ++i)
            {
                var item = new [TreeViewItem](IMGUI.Controls.TreeViewItem.html)(i, 0, i.ToString());
                allItems.Add(item);
            }  
      
            SetupParentsAndChildrenFromDepths(root, allItems);
            return root;
        }  
      
        protected override void RowGUI([RowGUIArgs](IMGUI.Controls.TreeView.RowGUIArgs.html) args)
        {
            var prop = m_Property.GetArrayElementAtIndex(args.item.id);
            for (int i = 0; i < args.GetNumVisibleColumns(); ++i)
            {
                int col = args.GetColumn(i);
                var rect = args.GetCellRect(i);  
      
                if (col == 0)
                {
                    [GUI.Label](GUI.Label.html)(rect, args.row.ToString());
                }
                else
                {
                    [EditorGUI.PropertyField](EditorGUI.PropertyField.html)(rect, prop, [GUIContent.none](GUIContent-none.html));
                }
            }
        }
    }  
      
    // Shows how we can use a [TreeView](IMGUI.Controls.TreeView.html) to draw a large list of items.
    [[CustomEditor](CustomEditor.html)(typeof(ExampleBehaviourScript))]
    [[CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class NewBehaviourScriptEditor : [Editor](Editor.html)
    {
        NewBehaviourScriptEditorTreeView m_TreeView;
        [SerializedProperty](SerializedProperty.html) m_Size;  
      
        void OnEnable()
        {
            var listProperty = serializedObject.FindProperty("exampleList");
            m_Size = serializedObject.FindProperty("exampleList.Array.size");
            m_TreeView = new NewBehaviourScriptEditorTreeView(listProperty);
            [Undo.undoRedoPerformed](Undo-undoRedoPerformed.html) += m_TreeView.Reload;
        }  
      
        void OnDisable()
        {
            if (m_TreeView != null)
                [Undo.undoRedoPerformed](Undo-undoRedoPerformed.html) -= m_TreeView.Reload;
        }  
      
        public override void OnInspectorGUI()
        {
            serializedObject.Update();
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            int newSize = [EditorGUILayout.IntField](EditorGUILayout.IntField.html)("Size", m_Size.intValue);
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                m_Size.intValue = newSize;
                m_TreeView.Reload();
            }  
      
            var rect = [EditorGUILayout.GetControlRect](EditorGUILayout.GetControlRect.html)(false, m_TreeView.totalHeight);
            m_TreeView.OnGUI(rect);
            serializedObject.ApplyModifiedProperties();
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

