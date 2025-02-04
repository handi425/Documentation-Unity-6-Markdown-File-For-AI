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

#  [EditorWindow](EditorWindow.html).OnSelectionChange()

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

### Description

Called whenever the selection has changed.

![](../StaticFiles/ScriptRefImages/SelectionChange.png)  
_Saves the current selection and load it later with a simple click._

    
    
    // Simple example that lets you save the current selection and load it.
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.UIElements;
    
    public class OnSelectionChangeExample : [EditorWindow](EditorWindow.html)
    {
        private int[] selectionIDs;
    
        [[MenuItem](MenuItem.html)("Examples/[Selection](Selection.html) Saver")]
        private static void Init()
        {
            OnSelectionChangeExample window = (OnSelectionChangeExample)GetWindow(typeof(OnSelectionChangeExample));
            window.Show();
        }
    
        void CreateGUI()
        {
            var buttonSave = new [Button](UIElements.Button.html)();
            buttonSave.text = "Save";
            buttonSave.clicked += () => SaveSelection();
            rootVisualElement.Add(buttonSave);
            
            var buttonLoad = new [Button](UIElements.Button.html)();
            buttonLoad.text = "Load";
            buttonLoad.clicked += () => LoadLastSavedSelection();
            rootVisualElement.Add(buttonLoad);
    
            // Initialize selectionIDs at least once
            OnSelectionChange();
        }
    
        void OnSelectionChange()
        {
            selectionIDs = [Selection.instanceIDs](Selection-instanceIDs.html);
        }
    
        private void SaveSelection()
        {
            var saveStr = "";
    
            foreach (int i in selectionIDs)
            {
                saveStr += i + ";";
            }
    
            saveStr = saveStr.TrimEnd(char.Parse(";"));
            [EditorPrefs.SetString](EditorPrefs.SetString.html)("SelectedIDs", saveStr);
        }
    
        private void LoadLastSavedSelection()
        {
            string[] strIDs = [EditorPrefs.GetString](EditorPrefs.GetString.html)("SelectedIDs").Split(char.Parse(";"));
    
            int[] ids = new int[strIDs.Length];
            for (var i = 0; i < strIDs.Length; i++)
            {
                if (!string.IsNullOrEmpty(strIDs[i]))
                    ids[i] = int.Parse(strIDs[i]);
            }
    
            [Selection.instanceIDs](Selection-instanceIDs.html) = ids;
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

