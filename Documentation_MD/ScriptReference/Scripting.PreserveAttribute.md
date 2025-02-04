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

# PreserveAttribute

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

PreserveAttribute prevents byte code stripping from removing a class, method,
field, or property.

When you create a build, Unity will try to strip unused code from your
project. This is great to get small builds. However, sometimes you want some
code to not be stripped, even if it looks like it is not used. This can happen
for instance if you use reflection to call a method, or instantiate an object
of a certain class. You can apply the [Preserve] attribute to classes,
methods, fields and properties. In addition to using PreserveAttribute, you
can also use the traditional method of a link.xml file to tell the linker to
not remove things. PreserveAttribute and link.xml work for both the Mono and
IL2CPP scripting backends.  
  
For more details on [Preserve] and link.xml see [Managed Code
Stripping](../Manual/ManagedCodeStripping.html)

    
    
    using UnityEngine;
    using System.Collections;
    using System.Reflection;
    using UnityEngine.Scripting;  
      
    public class NewBehaviourScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            ReflectionExample.InvokeBoinkByReflection();
        }
    }  
      
    public class ReflectionExample
    {
        static public void InvokeBoinkByReflection()
        {
            typeof(ReflectionExample).GetMethod("Boink", BindingFlags.NonPublic | BindingFlags.Static).Invoke(null, null);
        }  
      
        // No other code directly references the Boink method, so when when stripping is enabled,
        // it will be removed unless the [Preserve] attribute is applied.
        [Preserve]
        static void Boink()
        {
            [Debug.Log](Debug.Log.html)("Boink");
        }
    }
    

For 3rd party libraries that do not want to take on a dependency on
UnityEngine.dll, it is also possible to define their own PreserveAttribute.
The code stripper will respect that too, and it will consider any attribute
with the exact name "PreserveAttribute" as a reason not to strip the thing it
is applied on, regardless of the namespace or assembly of the attribute.

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

