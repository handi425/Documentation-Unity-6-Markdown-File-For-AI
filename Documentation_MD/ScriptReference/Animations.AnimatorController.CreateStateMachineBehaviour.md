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

#
[AnimatorController](Animations.AnimatorController.html).CreateStateMachineBehaviour

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

public static int CreateStateMachineBehaviour([MonoScript](MonoScript.html)
script);

### Parameters

script | MonoScript class to instantiate.  
---|---  
  
### Returns

**int** Returns instance id of created object, returns 0 if something is not
valid.

### Description

This function will create a StateMachineBehaviour instance based on the class
define in this script.

This function will validate that the monoscript is a valid statemachine
behaviour, the class must be a sub class of StateMachineBehaviour and
shouldn't be a generic. Additional resources:
[StateMachineBehaviour](StateMachineBehaviour.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Animations;
    using UnityEngine;  
      
    public class AddSMB
    {
        public void DoAddStateMachineBehaviour(UnityEditor.Animations.AnimatorState state, [MonoScript](MonoScript.html) monoScript)
        {
            if (state == null)
                return;  
      
            int instanceID = [AnimatorController.CreateStateMachineBehaviour](Animations.AnimatorController.CreateStateMachineBehaviour.html)(monoScript);
            if (instanceID == 0)
            {
                [Debug.LogError](Debug.LogError.html)("Could not create state machine behaviour " + monoScript.name);
                return;
            }  
      
            state.AddStateMachineBehaviour(monoScript.GetClass());  
      
            var obj = [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(instanceID);
            if (obj == null)
                [Debug.LogError](Debug.LogError.html)("No object could be found with instance id: " + instanceID);
            else
                [AssetDatabase.AddObjectToAsset](AssetDatabase.AddObjectToAsset.html)(obj, state.ToString());
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

