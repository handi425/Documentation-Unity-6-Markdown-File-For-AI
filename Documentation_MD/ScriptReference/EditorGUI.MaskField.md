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

#  [EditorGUI](EditorGUI.html).MaskField

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

public static int MaskField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, int mask, string[] displayedOptions,
[GUIStyle](GUIStyle.html) style = EditorStyles.popup);

## Declaration

public static int MaskField([Rect](Rect.html) position, string label, int
mask, string[] displayedOptions, [GUIStyle](GUIStyle.html) style =
EditorStyles.popup);

## Declaration

public static int MaskField([Rect](Rect.html) position, int mask, string[]
displayedOptions, [GUIStyle](GUIStyle.html) style = EditorStyles.popup);

### Parameters

position | Rectangle on the screen to use for this control.  
---|---  
label | Label for the field.  
mask | The current mask to display.  
displayedOption | A string array containing the labels for each flag.  
style | Optional [GUIStyle](GUIStyle.html).  
displayedOptions | A string array containing the labels for each flag.  
  
### Returns

**int** The value modified by the user.

### Description

Makes a field for masks.

**Note:** The mask values for the flags associated with each option in the
menu will be consecutive powers of 2 starting with 1, i.e. 1, 2, 4, 8, 16, and
so on.  
  
![](../StaticFiles/ScriptRefImages/MaskField.png)  
_Simple window that shows the mask field._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    class SimpleMaskUsage : [EditorWindow](EditorWindow.html)
    {
        int flags = 0;
        string[] options = { "CanJump", "CanShoot", "CanSwim" };  
      
        [[MenuItem](MenuItem.html)("Examples/Mask Field Usage")]
        static void Init()
        {
            var window = GetWindow<SimpleMaskUsage>();
            window.Show();
        }  
      
        void OnGUI()
        {
            flags = [EditorGUI.MaskField](EditorGUI.MaskField.html)(new [Rect](Rect.html)(0, 0, 300, 20), "Player [Flags](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)", flags, options);
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

