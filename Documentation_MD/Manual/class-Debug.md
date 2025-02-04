[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-Debug.html)
  * [中文](/cn/current/Manual/class-Debug.html)
  * [日本語](/ja/current/Manual/class-Debug.html)
  * [한국어](/kr/current/Manual/class-Debug.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-Debug.html)
  * [中文](/cn/current/Manual/class-Debug.html)
  * [日本語](/ja/current/Manual/class-Debug.html)
  * [한국어](/kr/current/Manual/class-Debug.html)

  * [Scripting](scripting.html)
  * [Debugging and diagnostics](debugging-and-diagnostics.html)
  * The Debug class

[](managed-code-debugging.html)

Debug C# code in Unity

[](log-files.html)

Log files reference

# The Debug class

[Switch to Scripting](../ScriptReference/Debug.html "Go to Debug page in the
Scripting Reference")

The Debug class allows you to visualise information in the Editor that may
help you understand or investigate what is going on in your project while it
is running. For example, you can use it to print messages into the Console
window, draw visualization lines in the **Scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view and Game view, and pause Play Mode
in the Editor from script.

This page provides an overview of the Debug class and its common uses when
scripting with it. For an exhaustive reference of every member of the Debug
class, see the [Debug script reference](../ScriptReference/Debug.html).

## Logging errors, warnings and messages

Unity itself sometimes logs errors, warnings and messages to the Console
window. The Debug class provides you with the ability to do exactly the same
from your own code, as shown below:

    
    
    Debug.Log("This is a log message.");
    Debug.LogWarning("This is a warning message!");
    Debug.LogError("This is an error message!");
    

The three types (error, warning, and message) each have their own icon type in
the Console window.

![](../uploads/Main/ConsoleShowingMessageWarningAndError.png)

Everything that is written to the Console Window (by Unity, or your own code)
is also written to a [Log File](log-files.html).

If you have **Error Pause** enabled in the Console, any errors that you write
to the Console via the Debug class will cause Unity’s Play Mode to pause.

You can also optionally provide a second parameter to these log methods to
indicate that the message is associated with a particular **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), like this:

    
    
    using UnityEngine;
    
    public class DebugExample : MonoBehaviour
    {    void Start()
        {
            Debug.LogWarning("I come in peace!", this.gameObject);
        }
    }
    

The benefit of this is that when you click the message in the console, the
GameObject you associated with that message is highlighted in the Hierarchy,
allowing you to identify which GameObject the message related to. In the image
below you can see that clicking the “I come in peace!” warning message
highlights the “Alien (8)” GameObject.

![](../uploads/Main/ConsoleMessageWithContextGameObject.png)

The Debug class also offers two methods for drawing lines in the **Scene
view** An interactive view into the world you are creating. You use the Scene
View to select and position scenery, characters, cameras, lights, and all
other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) and Game view. These are
[DrawLine](../ScriptReference/Debug.DrawLine.html) and
[DrawRay](../ScriptReference/Debug.DrawRay.html).

In this example, a script has been added to every Sphere GameObject in the
scene, which uses Debug.DrawLine to indicate its vertical distance from the
plane where Y equals zero. Note that the last parameter in this example is the
duration in seconds that the line should stay visible in the Editor.

    
    
    using UnityEngine;
    
    public class DebugLineExample : MonoBehaviour
    {
        // Start is called before the first frame update
        void Start()
        {
            float height = transform.position.y;
            Debug.DrawLine(transform.position, transform.position - Vector3.up * height, Color.magenta, 4);
        }
    }
    

And the result in the Scene view looks like this:

![](../uploads/Main/DebugDrawLineExampleInScene.png)

## Additional resources

  * [Console window](Console.html)A Unity Editor window that shows errors, warnings and other messages generated by Unity, or your own scripts. [More info](Console.html)  
See in [Glossary](Glossary.html#Consolewindow)

  * [Log files](log-files.html)

[](managed-code-debugging.html)

Debug C# code in Unity

[](log-files.html)

Log files reference

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

