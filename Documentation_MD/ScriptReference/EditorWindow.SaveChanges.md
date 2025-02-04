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

#  [EditorWindow](EditorWindow.html).SaveChanges

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

## Declaration

public void SaveChanges();

### Description

Performs a save action on the contents of the window.

Override SaveChanges() when using the
[EditorWindow.hasUnsavedChanges](EditorWindow-hasUnsavedChanges.html) property
so that a user will not lose unsaved work when a window is closed. The Editor
also calls this method internally when the user closes the window. Once
called, the Editor prompts the user to save changes. When overring the method,
be sure to call the base implementation or else the
[EditorWindow.hasUnsavedChanges](EditorWindow-hasUnsavedChanges.html) property
is not reset to false. Note, if the Editor has multiple prompts to the user to
save their changes, the Editor will call this method as part of a list of
changes that need saving. Unity cancels the save process for all remaining
prompts if this method throws an exception. In this case, you will find an
error message with the exception message displayed in a dialog box.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.UIElements;
    
    public class UnsavedChangesExampleWindow : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/[Editor](Editor.html) Window With Unsaved Changes")]
        static void Init()
        {
            UnsavedChangesExampleWindow window = (UnsavedChangesExampleWindow)[EditorWindow.GetWindowWithRect](EditorWindow.GetWindowWithRect.html)(typeof(UnsavedChangesExampleWindow), new [Rect](Rect.html)(100, 100, 400, 400));
    
            window.saveChangesMessage = "This window has unsaved changes. Would you like to save?";
            window.Show();
        }
    
        void CreateGUI()
        {
            var label = new [Label](UIElements.Label.html)();
            label.text = hasUnsavedChanges ? "I have changes!" : "No changes.";
            rootVisualElement.Add(label);
    
            var buttonCreate = new [Button](UIElements.Button.html)();
            buttonCreate.text = "Create unsaved changes";
            buttonCreate.clicked += () => {
                hasUnsavedChanges = true;
                [Debug.Log](Debug.Log.html)($"{this} has unsaved changes!!!");
            };
            rootVisualElement.Add(buttonCreate);
    
            var buttonSave = new [Button](UIElements.Button.html)();
            buttonSave.text = "Save";
            buttonSave.clicked += () => SaveChanges();
            rootVisualElement.Add(buttonSave);
    
            var buttonDiscard = new [Button](UIElements.Button.html)();
            buttonDiscard.text = "Discard";
            buttonDiscard.clicked += () => DiscardChanges();
            rootVisualElement.Add(buttonDiscard);
        }
    
        public override void SaveChanges()
        {
            // Your custom save procedures here
    
            [Debug.Log](Debug.Log.html)($"{this} saved successfully!!!");
            base.SaveChanges();
        }
    
        public override void DiscardChanges()
        {
            // Your custom procedures to discard changes
    
            [Debug.Log](Debug.Log.html)($"{this} discarded changes!!!");
            base.DiscardChanges();
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

