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

# BurstDiscardAttribute

class in Unity.Burst

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

### Description

The BurstDiscard attribute lets you remove a method or property from being
compiled to native code by the burst compiler.

By default, a job compiled with burst will compile all methods. In some cases,
you could have managed methods that cannot be compiled to native (e.g checking
for validity only valid in a managed environment or logging using managed
objects...etc) and should not be executed at runtime. In that case you can use
this attribute to mark a method or property as not compilable by the burst
compiler.

    
    
    using Unity.Burst;
    using Unity.Collections;
    using Unity.Jobs;
    using UnityEngine;  
      
    public struct MyJob : [IJob](Unity.Jobs.IJob.html)
    {
        // ...  
      
        [BurstDiscard]
        public void NotExecutedInNative()
        {
            [Debug.Log](Debug.Log.html)("This is a log from a managed job");
        }  
      
        public void Execute()
        {
            // The following method call will not be compiled
            NotExecutedInNative();
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

