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

# RequiredMemberAttribute

class in UnityEngine.Scripting

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

When a type is marked, all of its members with [RequiredMember] are marked.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine;
    using UnityEngine.Scripting;  
      
    public class NewBehaviourScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            new UsedFoo();
        }
    }  
      
    class UsedFoo
    {
        // Will survive managed code stripping because UsedFoo is used
        [RequiredMember]
        public int Field;  
      
        // Will survive managed code stripping because UsedFoo is used
        [RequiredMember]
        public void Method()
        {
        }  
      
        // The property, property getter method, and property setter method will survive managed code stripping because UsedFoo is used
        [RequiredMember]
        public int Property1 { get; set; }  
      
        // The property and property getter method will survive managed code stripping because UsedFoo is used
        public int Property2 { [RequiredMember] get; set; }  
      
        // The property and property setter method will survive managed code stripping because UsedFoo is used
        public int Property3 { get; [RequiredMember] set; }  
      
        // The event, the add method, and the remove method will survive managed code stripping because UsedFoo is used
        [RequiredMember]
        public event [EventHandler](Video.VideoPlayer.EventHandler.html) [Event](Event.html);
    }  
      
    class UnusedFoo
    {
        // Will not survive stripping because UnusedFoo is not used
        [RequiredMember]
        public int Field;  
      
        // Will not survive stripping because UnusedFoo is not used
        [RequiredMember]
        public void Method()
        {
        }  
      
        // Will not survive stripping because UnusedFoo is not used
        [RequiredMember]
        public int Property { get; set; }  
      
        // Will not survive stripping because UnusedFoo is not used
        [RequiredMember]
        public event [EventHandler](Video.VideoPlayer.EventHandler.html) [Event](Event.html);
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

