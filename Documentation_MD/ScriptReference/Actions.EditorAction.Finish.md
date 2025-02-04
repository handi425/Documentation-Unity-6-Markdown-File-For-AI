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

#  [EditorAction](Actions.EditorAction.html).Finish

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

public void
Finish([Actions.EditorActionResult](Actions.EditorActionResult.html) result);

### Parameters

result | The state that the [EditorAction](Actions.EditorAction.html) was finished in.  
---|---  
  
### Description

Finishes an [EditorAction](Actions.EditorAction.html) with a specific result.

Call this method to forcibly end an active
[EditorAction](Actions.EditorAction.html) with a
[EditorActionResult](Actions.EditorActionResult.html). A common use is when
implementing atomic actions that do not require interactivity.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Actions;
    
    public class SingleFrameActionSample : [EditorAction](Actions.EditorAction.html)
    {
        [[MenuItem](MenuItem.html)("Test/Start Single Frame [Action](Unity.Android.Gradle.Manifest.Action.html)")]
        static void StartEditorActionSample()
        {
            Start(new SingleFrameActionSample(4));
        }
    
        int m_Value;
    
        public SingleFrameActionSample(int value)
        {
            m_Value = value;
            Finish([EditorActionResult.Success](Actions.EditorActionResult.Success.html));
        }
    
        protected override void OnFinish([EditorActionResult](Actions.EditorActionResult.html) result)
        {
            m_Value += 2;
            [Debug.Log](Debug.Log.html)($"[Action](Unity.Android.Gradle.Manifest.Action.html) Finished [{result}] with value: {m_Value}");
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

