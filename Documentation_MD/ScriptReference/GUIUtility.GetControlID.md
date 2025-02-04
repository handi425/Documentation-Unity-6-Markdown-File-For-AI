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

#  [GUIUtility](GUIUtility.html).GetControlID

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

public static int GetControlID([FocusType](FocusType.html) focus);

## Declaration

public static int GetControlID([FocusType](FocusType.html) focus,
[Rect](Rect.html) position);

### Description

Get a unique ID for a control.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Prints a not used ID that can be assigned to a control  
      
        void OnGUI()
        {
            // Gets a ID for a control that cannot receive keyboard focus (A button)
            [Debug.Log](Debug.Log.html)("Available id: " + [GUIUtility.GetControlID](GUIUtility.GetControlID.html)([FocusType.Passive](FocusType.Passive.html)));
        }
    }
    

* * *

## Declaration

public static int GetControlID(int hint, [FocusType](FocusType.html) focus);

## Declaration

public static int GetControlID(int hint, [FocusType](FocusType.html)
focusType, [Rect](Rect.html) rect);

### Description

Get a unique ID for a control, using an integer as a hint to help ensure
correct matching of IDs to controls.

* * *

## Declaration

public static int GetControlID([GUIContent](GUIContent.html) contents,
[FocusType](FocusType.html) focus);

## Declaration

public static int GetControlID([GUIContent](GUIContent.html) contents,
[FocusType](FocusType.html) focus, [Rect](Rect.html) position);

### Description

Get a unique ID for a control, using a the label content as a hint to help
ensure correct matching of IDs to controls.

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

