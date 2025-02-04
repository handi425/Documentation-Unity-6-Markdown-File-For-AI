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

#  [SettingsProvider](SettingsProvider.html).OnDeactivate

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

public void OnDeactivate();

### Description

Use this function to implement a handler for when the user clicks on another
setting or when the Settings window closes.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.UIElements;  
      
    class SimpleIMGUISettingsProvider : [SettingsProvider](SettingsProvider.html)
    {
        [SerializedObject](SerializedObject.html) m_Settings;
        const string k_MyCustomSettingsPath = "Assets/[Editor](Editor.html)/MyCustomSettings.asset";
        public SimpleIMGUISettingsProvider(string path, [SettingsScope](SettingsScope.html) scope = [SettingsScope.User](SettingsScope.User.html))
            : base(path, scope) {}  
      
        public override void OnActivate(string searchContext, [VisualElement](UIElements.VisualElement.html) rootElement)
        {
            // Called when the user clicks on the MyCustom element in the [Settings](CameraEditor.Settings.html) window.
            m_Settings = new [SerializedObject](SerializedObject.html)([AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(k_MyCustomSettingsPath));
        }  
      
        public override void OnDeactivate()
        {
            // User selected another settings or closed the [Settings](CameraEditor.Settings.html) window.
            m_Settings = null;
        }  
      
        public override void OnGUI(string searchContext)
        {
            // Use IMGUI to display UI:
            [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(m_Settings.FindProperty("m_Number"), new [GUIContent](GUIContent.html)("My Number"));
            [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(m_Settings.FindProperty("m_SomeString"), new [GUIContent](GUIContent.html)("Some string"));
            m_Settings.ApplyModifiedPropertiesWithoutUndo();
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

