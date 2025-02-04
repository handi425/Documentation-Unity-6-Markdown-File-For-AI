[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/gizmos-and-handles.html)
  * [中文](/cn/current/Manual/gizmos-and-handles.html)
  * [日本語](/ja/current/Manual/gizmos-and-handles.html)
  * [한국어](/kr/current/Manual/gizmos-and-handles.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/gizmos-and-handles.html)
  * [中文](/cn/current/Manual/gizmos-and-handles.html)
  * [日本語](/ja/current/Manual/gizmos-and-handles.html)
  * [한국어](/kr/current/Manual/gizmos-and-handles.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * Gizmos and Handles

[](class-random.html)

Using randomness

[](null-reference-exception.html)

Null references

# Gizmos and Handles

The Gizmos and Handles classes allows you to draw lines and shapes in the
**Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view and Game view, as well as
interactive handles and controls. These two classes together provide a way for
you to extend what is shown in these views and build interactive tools to edit
your project in any way you like. For example, rather than entering numbers in
the **inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), you could create a draggable
circle radius gizmo around a non-player character in a game, which represents
the area within which they can hear or see the player.

This page provides a simple overview of the Gizmos and Handles classes. For
full documentation and an exhaustive reference of every member of the Gizmos
and Handles classes, see the script reference pages for
[Gizmos](../ScriptReference/Gizmos.html)A graphic overlay associated with a
GameObject in a Scene, and displayed in the Scene View. Built-in scene tools
such as the move tool are Gizmos, and you can create custom Gizmos using
textures or scripting. Some Gizmos are only drawn when the GameObject is
selected, while other Gizmos are drawn by the Editor regardless of which
GameObjects are selected. [More info](GizmosMenu.html#GizmosIcons)  
See in [Glossary](Glossary.html#Gizmo) and
[Handles](../ScriptReference/Handles.html).

## Gizmos

The Gizmos class allows you to draw lines, spheres, cubes, icons, textures and
meshes into the **Scene view** An interactive view into the world you are
creating. You use the Scene View to select and position scenery, characters,
cameras, lights, and all other types of Game Object. [More
info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) to use as debugging, set-up aids,
or tools while developing your project.

For example, to draw a 10 unit yellow wire cube around a **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), you would use this code:

    
    
    using UnityEngine;
    public class GizmosExample : MonoBehaviour
    {
        void OnDrawGizmosSelected()
        {
            // Draw a yellow cube at the transform position
            Gizmos.color = Color.yellow;
            Gizmos.DrawWireCube(transform.position, new Vector3(10, 10, 10));
        }
    }
    

And here is how that cube looks when placed on a Directional Light GameObject.

![A light GameObject with an extra script applied which draws a cube gizmo
around its position](../uploads/Main/ScriptingGizmoExample.png) A light
GameObject with an extra script applied which draws a cube gizmo around its
position

See the [Gizmos script reference page](../ScriptReference/Gizmos.html) for the
full documentation on how to use Gizmos.

## Handles

Handles are similar to Gizmos, but provide more functionality in terms of
interactivity and manipulation. The 3D controls that Unity itself provides to
manipulate items in the Scene view are a combination of Gizmos and Handles.
There are a number of built-in Handle GUIs, such as the familiar tools to
position, scale and rotate an object via the **Transform component** A
Transform component determines the Position, Rotation, and Scale of each
object in the scene. Every GameObject has a Transform. [More info](class-
Transform.html)  
See in [Glossary](Glossary.html#TransformComponent). However, you can define
your own Handle GUIs to use with custom component editors. Such GUIs can be a
very useful way to edit procedurally-generated Scene content, “invisible”
items and groups of related objects, such as waypoints and location markers.

For example, here is how you could create an arc area with an arrowhead
handle, allowing you to modify a “shield area” in the scene view:

    
    
    using UnityEditor;
    using UnityEngine;
    using System.Collections;
    
    //this class should exist somewhere in your project
    public class WireArcExample : MonoBehaviour
    {
        public float shieldArea;
    }
    
    // Create a 180 degrees wire arc with a ScaleValueHandle attached to the disc
    // that lets you modify the "shieldArea" value in the WireArcExample
    [CustomEditor(typeof(WireArcExample))]
    public class DrawWireArc : Editor
    {
        void OnSceneGUI()
        {
            Handles.color = Color.red;
            WireArcExample myObj = (WireArcExample)target;
            Handles.DrawWireArc(myObj.transform.position, myObj.transform.up, -myObj.transform.right, 180, myObj.shieldArea);
            myObj.shieldArea = (float)Handles.ScaleValueHandle(myObj.shieldArea, myObj.transform.position + myObj.transform.forward * myObj.shieldArea, myObj.transform.rotation, 1, Handles.ConeHandleCap, 1);
        }
    }
    

![An example of an Arc handle and an Scale
handle](../uploads/Main/ScriptingHandlesExample.png) An example of an Arc
handle and an Scale handle

See the [Handles script reference page](../ScriptReference/Handles.html) for
the full documentation on how to use Handles.

[](class-random.html)

Using randomness

[](null-reference-exception.html)

Null references

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

