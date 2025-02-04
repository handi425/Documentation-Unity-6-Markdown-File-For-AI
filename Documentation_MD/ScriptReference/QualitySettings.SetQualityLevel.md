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

#  [QualitySettings](QualitySettings.html).SetQualityLevel

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

[Switch to Manual](../Manual/class-QualitySettings.html "Go to QualitySettings
Component in the Manual")

## Declaration

public static void SetQualityLevel(int index, bool applyExpensiveChanges =
true);

### Parameters

index | Quality index to set.  
---|---  
applyExpensiveChanges | Should expensive changes be applied (Anti-aliasing etc).  
  
### Description

Sets a new graphics quality level.

The list of quality levels can be found by going to **Edit** > **Project
Settings** > **Quality**. You can add, remove or edit these.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            string[] names = [QualitySettings.names](QualitySettings-names.html);
            [GUILayout.BeginVertical](GUILayout.BeginVertical.html)();
            for (int i = 0; i < names.Length; i++)
            {
                if ([GUILayout.Button](GUILayout.Button.html)(names[i]))
                {
                    [QualitySettings.SetQualityLevel](QualitySettings.SetQualityLevel.html)(i, true);
                }
            }
            [GUILayout.EndVertical](GUILayout.EndVertical.html)();
        }
    }
    

Note that changing the quality level can be an expensive operation if the new
level has different anti-aliasing setting. It's fine to change the level when
applying in-game quality options, but if you want to dynamically adjust
quality level at runtime, pass false to applyExpensiveChanges so that
expensive changes are not always applied.  
  
When building a player quality levels that are not used for that platform are
stripped. You should not expect a given quality setting to be at a given
index. It's best to query the available quality settings and use the returned
index.  
  
Additional resources: [GetQualityLevel](QualitySettings.GetQualityLevel.html).

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

