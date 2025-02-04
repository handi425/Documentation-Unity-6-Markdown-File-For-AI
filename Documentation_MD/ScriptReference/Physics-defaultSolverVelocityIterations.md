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

#  [Physics](Physics.html).defaultSolverVelocityIterations

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

public static int defaultSolverVelocityIterations;

### Description

The defaultSolverVelocityIterations affects how accurately the Rigidbody
joints and collision contacts are resolved. (default 1). Must be positive.

Increasing this value will result in higher accuracy of the resulting exit
velocity after a Rigidbody bounce. If you are experiencing issues with jointed
Rigidbodies or Ragdolls moving too much after collisions you can try to
increase this value.  
  
This value is usually changed in `Edit->Project Settings->Physics` inspector
instead of from scripts.  
  
**Note:** Changing the defaultSolverVelocityIterations does not affect already
created Rigidbodies. To change an existing Rigidbody please use
[Rigidbody.solverVelocityIterations](Rigidbody-solverVelocityIterations.html).  
  
Additional resources: [Physics.defaultSolverIterations](Physics-
defaultSolverIterations.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Physics.defaultSolverVelocityIterations](Physics-defaultSolverVelocityIterations.html) = 10;
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

