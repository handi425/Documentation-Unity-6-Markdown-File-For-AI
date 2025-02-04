[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/Tags.html)
  * [中文](/cn/current/Manual/Tags.html)
  * [日本語](/ja/current/Manual/Tags.html)
  * [한국어](/kr/current/Manual/Tags.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/Tags.html)
  * [中文](/cn/current/Manual/Tags.html)
  * [日本語](/ja/current/Manual/Tags.html)
  * [한국어](/kr/current/Manual/Tags.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with scenes](working-with-scenes.html)
  * Tags

[](layermask-remove.html)

Remove a layer from a layerMask

[](Cameras.html)

Cameras

# Tags

A tag is a reference word which you can assign to one or more **GameObjects**
The fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject). For example, you might define
“Player” tags for player-controlled characters and an “Enemy” tag for non-
player-controlled characters. You might define items the player can collect in
a **Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) with a “Collectable” tag. You can use
any word you want as a tag. You can even use short phrases, but you might need
to widen the Inspector to see the tag’s full name. A GameObject can only have
one tag assigned to it.

Tags help you identify GameObjects for scripting purposes. They ensure you
don’t need to manually add GameObjects to a script’s exposed properties with
drag and drop, so you save time when you use the same script code in multiple
GameObjects.

Tags are useful for triggers in [Collider](CollidersOverview.html)An invisible
shape that is used to handle physical collisions for an object. A collider
doesn’t need to be exactly the same shape as the object’s mesh - a rough
approximation is often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) control **scripts** A piece of code
that allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) that need to determine if the player
interacts with an enemy, a prop, or a collectable, for example.

You can use the
[GameObject.FindWithTag](../ScriptReference/GameObject.FindWithTag.html)
function to find any GameObject that contains a tag you specify. The following
example uses `GameObject.FindWithTag()`. It instantiates `respawnPrefab` at
the location of GameObjects with the “Respawn” tag.

    
    
    using UnityEngine;
    using System.Collections;
    
    public class Example : MonoBehaviour {
        public GameObject respawnPrefab;
        public GameObject respawn;
        void Start() {
            if (respawn == null)
                respawn = GameObject.FindWithTag("Respawn");
    
            Instantiate(respawnPrefab, respawn.transform.position, respawn.transform.rotation) as GameObject;
        }
    }
    

## Create new Tags

The **Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) displays the **Tag** and **Layer**
Layers in Unity can be used to selectively opt groups of GameObjects in or out
of certain processes or calculations. This includes camera rendering,
lighting, physics collisions, or custom calculations in your own code. [More
info](Layers.html)  
See in [Glossary](Glossary.html#Layer) dropdown menus below the name of a
GameObject.

![](../uploads/Main/tag-dropdown.png)

To create a new tag, select **Add Tag…**. This opens the [Tag and Layer
Manager](class-TagManager.html) in the Inspector. Once you name a tag, it
can’t be renamed later.

Layers are similar to tags, but are used to define how Unity renders
GameObjects in the Scene. Refer to documentation on the [Layers](Layers.html)
page for more information.

## Apply a Tag

The **Inspector** shows the **Tag** and **Layer** dropdown menus just below
the name of a GameObject. To apply an existing tag to a GameObject, open the
**Tags** dropdown and choose the tag you want to apply. The GameObject is now
associated with this tag.

## Understand built-in tags

The Editor includes the following built-in tags which don’t appear in the Tag
Manager:

  * **Untagged**
  * **Respawn**
  * **Finish**
  * **EditorOnly**
  * **MainCamera**
  * **Player**
  * **GameController**

Some built-in tags like **MainCamera** and **EditorOnly** have unique
functions.

The Editor caches GameObjects tagged with the **MainCamera** tag internally.
When you access [Camera.main](../ScriptReference/Camera-main.html), the Editor
returns the first valid result from its cache. Refer to
[Camera.main](../ScriptReference/Camera-main.html) to learn more.

A GameObject tagged with **EditorOnly** in a Scene is destroyed when the game
builds. Any child GameObjects of a GameObject tagged with **EditorOnly** are
also destroyed when the game builds.

## Additional resources

  * [Camera.main](../ScriptReference/Camera-main.html)
  * [Introduction to collision](CollidersOverview.html)
  * [GameObject.FindWithTag](../ScriptReference/GameObject.FindWithTag.html)
  * [Layers](Layers.html)

[](layermask-remove.html)

Remove a layer from a layerMask

[](Cameras.html)

Cameras

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

