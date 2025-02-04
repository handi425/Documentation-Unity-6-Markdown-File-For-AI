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

#  [Editor](Editor.html).DiscardChanges

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

public void DiscardChanges();

### Description

Discards unsaved changes to the contents of the editor.

Override DiscardChanges() to discard unsaved work when an editor is closed.
When you override this method, call the base implementation. Otherwise the
[Editor.hasUnsavedChanges](Editor-hasUnsavedChanges.html) property is not
reset to false. Note, if the Editor has multiple prompts to the user to
discard their changes, the Editor will call this method as part of a list of
changes that need to be discarded. If this method throws an exception, Unity
cancels the discard process for all remaining prompts. In that case, a dialog
box displays an error message with the exception message.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    [CreateAssetMenu]
    public class UnsavedChangesExampleSO : [ScriptableObject](ScriptableObject.html)
    {}  
      
    [[CustomEditor](CustomEditor.html)(typeof(UnsavedChangesExampleSO))]
    public class UnsavedChangesExampleEditor : UnityEditor.Editor
    {
        void OnEnable()
        {
            saveChangesMessage = "This editor has unsaved changes. Would you like to save?";
        }  
      
        void OnInspectorGUI()
        {
            saveChangesMessage = [EditorGUILayout.TextField](EditorGUILayout.TextField.html)(saveChangesMessage);  
      
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)(hasUnsavedChanges ? "I have changes!" : "No changes.", [EditorStyles.wordWrappedLabel](EditorStyles-wordWrappedLabel.html));
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Try to change selection.");  
      
            using (new [EditorGUI.DisabledScope](EditorGUI.DisabledScope.html)(hasUnsavedChanges))
            {
                if ([GUILayout.Button](GUILayout.Button.html)("Create unsaved changes"))
                    hasUnsavedChanges = true;
            }  
      
            using (new [EditorGUI.DisabledScope](EditorGUI.DisabledScope.html)(!hasUnsavedChanges))
            {
                if ([GUILayout.Button](GUILayout.Button.html)("Save"))
                    SaveChanges();  
      
                if ([GUILayout.Button](GUILayout.Button.html)("Discard"))
                    DiscardChanges();
            }
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

