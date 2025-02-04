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

#  [EditorPrefs](EditorPrefs.html).SetFloat

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

public static void SetFloat(string key, float value);

### Parameters

key | Name of key to write float into.  
---|---  
value | Float value to write into the storage.  
  
### Description

Sets the float value of the preference identified by `key`.

    
    
    // Simple script that allows a float value to be editted
    // in a slider. The final value is written into the [Editor](Editor.html) Preferences.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using [System](Rendering.VirtualTexturing.System.html);  
      
    public class SetFloatExample : [EditorWindow](EditorWindow.html)
    {
        static float floatValue = 0.0f;  
      
        [[MenuItem](MenuItem.html)("Examples/Preferences SetFloat Example")]
        static void Init()
        {
            [Rect](Rect.html) r = new [Rect](Rect.html)(10, 10, 200, 100);
            SetFloatExample window = (SetFloatExample)[EditorWindow.GetWindowWithRect](EditorWindow.GetWindowWithRect.html)(typeof(SetFloatExample), r);
            window.Show();
        }  
      
        void Awake()
        {
            floatValue = [EditorPrefs.GetFloat](EditorPrefs.GetFloat.html)("FloatExample", floatValue);
        }  
      
        void OnGUI()
        {
            floatValue = [EditorGUILayout.Slider](EditorGUILayout.Slider.html)(floatValue, -1.0f, 1.0f);
            if ([GUILayout.Button](GUILayout.Button.html)("Save float " + Convert.ToString(floatValue) + "?"))
            {
                [EditorPrefs.SetFloat](EditorPrefs.SetFloat.html)("FloatExample", floatValue);
            }
            if ([GUILayout.Button](GUILayout.Button.html)("Close"))
                this.Close();
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

