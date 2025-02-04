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

# RuntimeInitializeOnLoadMethodAttribute

class in UnityEngine

/

Inherits from:[Scripting.PreserveAttribute](Scripting.PreserveAttribute.html)

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

Use this attribute to get a callback when the runtime is starting up and
loading the first scene.

Use the various options for
[RuntimeInitializeLoadType](RuntimeInitializeLoadType.html) to control when
the method is invoked in the startup sequence.  
  
The following list shows the execution order of the
[RuntimeInitializeLoadType](RuntimeInitializeLoadType.html) callbacks:

  1. First various low level systems are initialized (window, assemblies, gfx etc.)
  2. Then **SubsystemRegistration** and **AfterAssembliesLoaded** callbacks are invoked.
  3. More setup (input systems etc.)
  4. Then **BeforeSplashScreen** callback is invoked.
  5. Now the first scene starts loading.
  6. Then **BeforeSceneLoad** callback is invoked. Here objects of the scene is loaded but Awake() has not been called yet. All objects are considered inactive here.
  7. Now Awake() and OnEnable() are invoked on MonoBehaviours.
  8. Then **AfterSceneLoad** callback is invoked. Here objects of the scene are considered fully loaded and setup. Active objects can be found with FindObjectsByType.

The above details are when starting up a Player build. When entering Play mode
in the Editor the same invocations are ensured.  
  
The default callback invocation time is
[RuntimeInitializeLoadType.AfterSceneLoad](RuntimeInitializeLoadType.AfterSceneLoad.html).
The execution order within each of the
[RuntimeInitializeLoadType](RuntimeInitializeLoadType.html) callbacks is not
guaranteed.  
  
**Note:** Use the
[AlwaysLinkAssemblyAttribute](Scripting.AlwaysLinkAssemblyAttribute.html) on
package or precompiled assemblies that contain one or more methods with the
`[RuntimeInitializeOnLoadMethod]` attribute, but which may not contain types
used directly or indirectly in any scenes built for the project.  
  
Additional resources: [Managed code stripping](../Manual/managed-code-
stripping.html)

    
    
    // Demonstration of the RuntimeInitializeOnLoadMethod attribute
    using UnityEngine;  
      
    class MyClass
    {
        [RuntimeInitializeOnLoadMethod([RuntimeInitializeLoadType.BeforeSplashScreen](RuntimeInitializeLoadType.BeforeSplashScreen.html))]
        static void OnBeforeSplashScreen()
        {
            [Debug.Log](Debug.Log.html)("Before [SplashScreen](Rendering.SplashScreen.html) is shown and before the first scene is loaded.");
        }  
      
        [RuntimeInitializeOnLoadMethod([RuntimeInitializeLoadType.BeforeSceneLoad](RuntimeInitializeLoadType.BeforeSceneLoad.html))]
        static void OnBeforeSceneLoad()
        {
            [Debug.Log](Debug.Log.html)("First scene loading: Before Awake is called.");
        }  
      
        [RuntimeInitializeOnLoadMethod([RuntimeInitializeLoadType.AfterSceneLoad](RuntimeInitializeLoadType.AfterSceneLoad.html))]
        static void OnAfterSceneLoad()
        {
            [Debug.Log](Debug.Log.html)("First scene loaded: After Awake is called.");
        }  
      
        [RuntimeInitializeOnLoadMethod]
        static void OnRuntimeInitialized()
        {
            [Debug.Log](Debug.Log.html)("Runtime initialized: First scene loaded: After Awake is called.");
        }
    }
    

### Properties

[loadType](RuntimeInitializeOnLoadMethodAttribute-loadType.html)| Controling
the callback invocation time.  
---|---  
  
### Constructors

[RuntimeInitializeOnLoadMethodAttribute](RuntimeInitializeOnLoadMethodAttribute-
ctor.html)| Use the RuntimeInitializeLoadType to control when the callback is
invoked.  
---|---  
  
### Inherited Members

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

