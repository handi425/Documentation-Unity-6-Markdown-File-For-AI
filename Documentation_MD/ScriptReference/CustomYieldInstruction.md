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

# CustomYieldInstruction

class in UnityEngine

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

Base class for custom yield instructions to suspend coroutines.

[CustomYieldInstruction](CustomYieldInstruction.html) lets you implement
custom yield instructions to suspend coroutine execution until an event
happens. Under the hood, custom yield instruction is just another running
coroutine. To implement it, inherit from
[CustomYieldInstruction](CustomYieldInstruction.html) class and override
[keepWaiting](CustomYieldInstruction-keepWaiting.html) property. To keep
coroutine suspended return `true`. To let coroutine proceed with execution
return `false`. [keepWaiting](CustomYieldInstruction-keepWaiting.html)
property is queried each frame after
[MonoBehaviour.Update](MonoBehaviour.Update.html) and before
[MonoBehaviour.LateUpdate](MonoBehaviour.LateUpdate.html).  
  
This class requires Unity 5.3 or later.  
  
To keep coroutine suspended, return `true`. To let coroutine proceed with
execution, return `false`.

    
    
    // Example showing how a [CustomYieldInstruction](CustomYieldInstruction.html) script file
    // can be used.  This waits for the left button to go up and then
    // waits for the right button to go down.
    using System.Collections;
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetMouseButtonUp](Input.GetMouseButtonUp.html)(0))
            {
                [Debug.Log](Debug.Log.html)("Left mouse button up");
                StartCoroutine(waitForMouseDown());
            }
        }  
      
        public IEnumerator waitForMouseDown()
        {
            yield return new WaitForMouseDown();
            [Debug.Log](Debug.Log.html)("Right mouse button pressed");
        }
    }
    

The following script implements the overridable version of `keepWaiting`. This
c# implementation can be used by JS. In this case make sure this c# script is
in a folder such as `Plugins` so it is compiled before the JS script example
above.

    
    
    using UnityEngine;  
      
    public class WaitForMouseDown : [CustomYieldInstruction](CustomYieldInstruction.html)
    {
        public override bool keepWaiting
        {
            get
            {
                return ![Input.GetMouseButtonDown](Input.GetMouseButtonDown.html)(1);
            }
        }  
      
        public WaitForMouseDown()
        {
            [Debug.Log](Debug.Log.html)("Waiting for Mouse right button down");
        }
    }
    
    
    
    using System.Collections;
    using UnityEngine;
    using [System](Rendering.VirtualTexturing.System.html);  
      
    // Implementation of [WaitWhile](WaitWhile.html) yield instruction. This can be later used as:
    // yield return new [WaitWhile](WaitWhile.html)(() => Princess.isInCastle);
    class WaitWhile1 : [CustomYieldInstruction](CustomYieldInstruction.html)
    {
        Func<bool> m_Predicate;  
      
        public override bool keepWaiting { get { return m_Predicate(); } }  
      
        public WaitWhile1(Func<bool> predicate) { m_Predicate = predicate; }
    }
    

To have more control and implement more complex yield instructions you can
inherit directly from `System.Collections.IEnumerator` class. In this case,
implement `MoveNext()` method the same way you would implement
[keepWaiting](CustomYieldInstruction-keepWaiting.html) property. Additionally
to that, you can also return an object in `Current` property, that will be
processed by Unity's coroutine scheduler after executing `MoveNext()` method.
So for example if `Current` returned another object inheriting from
`IEnumerator`, then current enumerator would be suspended until the returned
one has completed.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections;  
      
    // Same [WaitWhile](WaitWhile.html) implemented by inheriting from IEnumerator.
    class WaitWhile2 : IEnumerator
    {
        Func<bool> m_Predicate;  
      
        public object Current { get { return null; } }  
      
        public bool MoveNext() { return m_Predicate(); }  
      
        public void Reset() {}  
      
        public WaitWhile2(Func<bool> predicate) { m_Predicate = predicate; }
    }
    

### Properties

[keepWaiting](CustomYieldInstruction-keepWaiting.html)| Indicates if coroutine
should be kept suspended.  
---|---  
  
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

