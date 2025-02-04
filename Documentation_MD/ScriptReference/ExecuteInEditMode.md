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

# ExecuteInEditMode

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

Causes a MonoBehaviour-derived class to execute in Edit mode in addition to at
runtime.

By default, MonoBehaviour [event functions](../Manual/event-functions.html)
only execute at runtime. Applying `ExecuteInEditMode` to a MonoBehaviour-
derived class causes the event functions for any instance of that class to
also execute in Edit mode.  
  
This attribute targets classes, but it only has an effect on classes that
inherit from [MonoBehaviour](MonoBehaviour.html).  
  
This attribute is not recommended because it is not compatible with editing in
prefab editing mode. The recommended alternative is
[ExecuteAlways](ExecuteAlways.html).  
  
If you're editing a prefab containing a MonoBehaviour with the
`ExecuteInEditMode` attribute in prefab editing mode and you then enter Play
mode, Unity exits prefab editing mode to prevent accidental modification to
the prefab caused by logic intended for Play mode only.  
  
To keep prefab editing mode open while in Play mode, use the
[ExecuteAlways](ExecuteAlways.html) attribute instead. If you do this, you
must take care to ensure your runtime MonoBehaviour code does not modify the
prefab you're editing in ways intended to occur only during gameplay. For more
details, refer to [ExecuteAlways](ExecuteAlways.html).  
  
In Edit mode, event functions are not called as frequently or under all the
same conditions as they are at runtime. Event functions are called under the
following conditions:

  * [Awake](MonoBehaviour.Awake.html) is called only when a new instance of the script component is created. This happens when Unity loads a scene that contains the component or when you create a new component in the Editor, for example through the **Component** menu.
  * [Update](MonoBehaviour.Update.html) is called on every redraw of the **Scene** view or **Game** view. This hapens when something in the scene changes, for example, the position of a GameObject or when you navigate the scene with the mouse or keys.
  * [OnGUI](MonoBehaviour.OnGUI.html) is called when the **Game** view receives a non-Editor-only [Event](Event.html) that it doesn't use and doesn't forward to the Editor's keyboard shortcut system. For example, `OnGUI` is called on receiving an instance of [EventType.ScrollWheel](EventType.ScrollWheel.html) that's not forwarded to [EventType.KeyDown](EventType.KeyDown.html) or [EventType.KeyUp](EventType.KeyUp.html). Events forwarded to the **Game** view are added to a queue and aren't guaranteed to be processed immediately.
  * [OnRenderObject](MonoBehaviour.OnRenderObject.html) and other rendering callback functions are called on every redraw of the **Scene** view or **Game** view.

See Also: [ExecuteAlways](ExecuteAlways.html),
[Application.IsPlaying](Application.IsPlaying.html),
[runInEditMode](MonoBehaviour-runInEditMode.html),
[EditorApplication.QueuePlayerLoopUpdate](EditorApplication.QueuePlayerLoopUpdate.html).

    
    
    // The PrintAwake script is placed on a [GameObject](GameObject.html). Usually, the Awake function is
    // called when the [GameObject](GameObject.html) with this script is initialized at runtime. Due to the [ExecuteInEditMode](ExecuteInEditMode.html)
    // attribute, the [Editor](Editor.html) also calls Awake when the script component is created via an [Editor](Editor.html) menu or when a scene that contains it is loaded.
    // The [Update](PlayerLoop.Update.html) function is called when the [Scene](SceneManagement.Scene.html) view needs to render, which happens when something in the scene changes or you navigate the scene with mouse or keyboard inputs.  
      
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class PrintAwake : [MonoBehaviour](MonoBehaviour.html)
    {
        void Awake()
        {
            [Debug.Log](Debug.Log.html)("[Editor](Editor.html) causes this Awake");
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [Debug.Log](Debug.Log.html)("[Editor](Editor.html) causes this [Update](PlayerLoop.Update.html)");
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

