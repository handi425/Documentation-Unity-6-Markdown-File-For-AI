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

#  [EditorGUILayout](EditorGUILayout.html).MaskField

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

public static int MaskField([GUIContent](GUIContent.html) label, int mask,
string[] displayedOptions, [GUIStyle](GUIStyle.html) style, params
GUILayoutOption[] options);

## Declaration

public static int MaskField(string label, int mask, string[] displayedOptions,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static int MaskField([GUIContent](GUIContent.html) label, int mask,
string[] displayedOptions, params GUILayoutOption[] options);

## Declaration

public static int MaskField(string label, int mask, string[] displayedOptions,
params GUILayoutOption[] options);

## Declaration

public static int MaskField(int mask, string[] displayedOptions,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static int MaskField(int mask, string[] displayedOptions, params
GUILayoutOption[] options);

### Parameters

label | Prefix label of the field.  
---|---  
mask | The current mask to display.  
displayedOption | A string array containing the labels for each flag.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Returns

**int** The value modified by the user.

### Description

Make a field for masks.

![](../StaticFiles/ScriptRefImages/MaskField.png)  
_Simple window that shows the mask field._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class MaskFieldExample : [EditorWindow](EditorWindow.html)
    {
        static int flags = 0;
        static string[] options = new string[] {"CanJump", "CanShoot", "CanSwim"};  
      
        [[MenuItem](MenuItem.html)("Examples/Mask Field usage")]
        static void Init()
        {
            MaskFieldExample window = (MaskFieldExample)GetWindow(typeof(MaskFieldExample));
            window.Show();
        }  
      
        void OnGUI()
        {
            flags = [EditorGUILayout.MaskField](EditorGUILayout.MaskField.html)("Player [Flags](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)", flags, options);  
      
            // [Display](Display.html) the flags in disabled toggles
            [GUI.enabled](GUI-enabled.html) = false;
            for (var i = 0; i < options.Length; i++)
            {
                var value = (flags & (1 << i)) != 0;
                [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)(options[i], value);
            }
            [GUI.enabled](GUI-enabled.html) = true;
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

