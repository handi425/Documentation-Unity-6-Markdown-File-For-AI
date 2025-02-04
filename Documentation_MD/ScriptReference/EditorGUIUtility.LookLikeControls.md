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

#  [EditorGUIUtility](EditorGUIUtility.html).LookLikeControls

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

**Obsolete** LookLikeControls and LookLikeInspector modes are deprecated.Use
EditorGUIUtility.labelWidth and EditorGUIUtility.fieldWidth to control label
and field widths.

## Declaration

public static void LookLikeControls(float _labelWidth, float _fieldWidth);

### Parameters

labelWidth | Width to use for prefixed labels.  
---|---  
fieldWidth | Width of text entries.  
  
### Description

Make all [EditorGUI](EditorGUI.html) look like regular controls.

This will make the default styles used by [EditorGUI](EditorGUI.html) look
like controls (e.g. [EditorGUI.Popup](EditorGUI.Popup.html) becomes a full
popup menu).  
  
![](../StaticFiles/ScriptRefImages/EditorGUIUtilityLookLikeControls.png)  
_Editor window with "LookLikeControls" look._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    
    // Simple editor window that shows the difference between
    // Look like controls and look like inspector  
      
    class LookLikeControlsInspector : [EditorWindow](EditorWindow.html)
    {
        int integer1 = 0;
        float float1 = 5.5f;  
      
        [[MenuItem](MenuItem.html)("Examples/Look Like Controls - Inspector")]
        static void Init()
        {
            var window = GetWindow<LookLikeControlsInspector>();
            window.Show();
        }  
      
        void OnGUI()
        {
            EditorGUIUtility.LookLikeInspector();
            [EditorGUILayout.TextField](EditorGUILayout.TextField.html)("Text Field:", "Hello There");
            [EditorGUILayout.IntField](EditorGUILayout.IntField.html)("Int Field:", integer1);
            [EditorGUILayout.FloatField](EditorGUILayout.FloatField.html)("Float Field:", float1);
            [EditorGUILayout.Space](EditorGUILayout.Space.html)();
            [EditorGUIUtility.LookLikeControls](EditorGUIUtility.LookLikeControls.html)();
            [EditorGUILayout.TextField](EditorGUILayout.TextField.html)("Text Field", "Hello There");
            [EditorGUILayout.IntField](EditorGUILayout.IntField.html)("Int Field:", integer1);
            [EditorGUILayout.FloatField](EditorGUILayout.FloatField.html)("Float Field:", float1);
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

