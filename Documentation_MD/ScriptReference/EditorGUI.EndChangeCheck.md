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

#  [EditorGUI](EditorGUI.html).EndChangeCheck

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

public static bool EndChangeCheck();

### Returns

**bool** Returns true if GUI state changed since the call to
[EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html), otherwise
false.

### Description

Ends a code block and checks for any GUI changes.

Use this in combination with
[EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html) to create a code
block that checks if the GUI state changed for just the controls contained in
the block.  
That is, unlike [GUI.changed](GUI-changed.html) which returns true for _any_
changes to the GUI state, this allows limiting the check to a specific set of
controls.

    
    
    using [UnityEditor](UnityEditor.html);  
      
    public class ExampleWindow : [EditorWindow](EditorWindow.html)
    {
        float sliderValue = 0;
        string labelText = "-";  
      
        [[MenuItem](MenuItem.html)("Window/Example Window")]
        static void Init()
        {
            var example = (ExampleWindow)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(ExampleWindow));
            example.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("New value", labelText);  
      
            // Start a code block to check for [GUI](GUI.html) changes
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();  
      
            sliderValue = [EditorGUILayout.Slider](EditorGUILayout.Slider.html)(sliderValue, 0, 1);  
      
            // End the code block and update the label if a change occurred
            // Note: This indicates user interaction with the slider but does not guarantee that a [SerializedProperty](SerializedProperty.html) has changed.
            // To have the updated value, call serializedObject.ApplyModifiedProperties().
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                labelText = sliderValue.ToString();
            }
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

