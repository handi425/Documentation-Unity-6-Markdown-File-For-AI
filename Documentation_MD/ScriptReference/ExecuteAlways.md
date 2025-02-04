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

# ExecuteAlways

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

Causes a MonoBehaviour-derived class to execute in Edit mode and prefab
editing mode in addition to at runtime.

By default, MonoBehaviour [event functions](../Manual/event-functions.html)
only execute at runtime. Applying `ExecuteAlways` to a MonoBehaviour-derived
class causes the event functions for any instance of that class to also
execute in Edit mode and Prefab mode.  
  
This attribute targets classes, but it only has an effect on classes that
inherit from [MonoBehaviour](MonoBehaviour.html).  
  
Use the `[ExecuteAlways]` attribute when you want your script to perform
actions or respond to events at authoring time, which are not necessarily
related to what happens at application runtime in the Editor's Play mode or a
standalone Player. Sometimes the runtime functionality of such a script is
identical to its Edit mode functionality, while other times they differ
greatly.  
  
It's important to ensure that a MonoBehaviour script using this attribute does
not have runtime code which could incorrectly execute and modify the parent
GameObject while it's being edited in Edit mode or prefab editing mode. To
avoid this, you can put your runtime code inside a conditional block that only
runs if [Application.IsPlaying](Application.IsPlaying.html) is `true` for the
script's own parent GameObject, as shown in the code exmple below.  
  
If your script makes use of static variables or Singleton patterns, you should
ensure that instances of the script that belong to the playing world and
instances that don't will not accidentally affect each other through those
variables or Singletons.  
  
In Edit mode, event functions are not called as frequently or under all the
same conditions as they are at runtime. Event functions are called under the
following conditions:

  * [Awake](MonoBehaviour.Awake.html) is called only when a new instance of the script component is created. This happens when Unity loads a scene that contains the component or when you create a new component in the Editor, for example through the **Component** menu.
  * [Update](MonoBehaviour.Update.html) is called on every redraw of the **Scene** view or **Game** view. This hapens when something in the scene changes, for example, the position of a GameObject or when you navigate the scene with the mouse or keys.
  * [OnGUI](MonoBehaviour.OnGUI.html) is called when the **Game** view receives a non-Editor-only [Event](Event.html) that it doesn't use and doesn't forward to the Editor's keyboard shortcut system. For example, `OnGUI` is called on receiving an instance of [EventType.ScrollWheel](EventType.ScrollWheel.html) that's not forwarded to [EventType.KeyDown](EventType.KeyDown.html) or [EventType.KeyUp](EventType.KeyUp.html). Events forwarded to the **Game** view are added to a queue and aren't guaranteed to be processed immediately.
  * [OnRenderObject](MonoBehaviour.OnRenderObject.html) and the other rendering callback functions are called on every redraw of the **Scene** view or **Game** view.

See Also: [Application.IsPlaying](Application.IsPlaying.html),
[runInEditMode](MonoBehaviour-runInEditMode.html),
[EditorApplication.QueuePlayerLoopUpdate](EditorApplication.QueuePlayerLoopUpdate.html).

    
    
    using UnityEngine;  
      
    [[ExecuteAlways](ExecuteAlways.html)]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            if ([Application.IsPlaying](Application.IsPlaying.html)(gameObject))
            {
                // Play logic
            }
            else
            {
                // [Editor](Editor.html) logic
            }
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

