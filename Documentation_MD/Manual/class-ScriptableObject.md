[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-ScriptableObject.html)
  * [中文](/cn/current/Manual/class-ScriptableObject.html)
  * [日本語](/ja/current/Manual/class-ScriptableObject.html)
  * [한국어](/kr/current/Manual/class-ScriptableObject.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-ScriptableObject.html)
  * [中文](/cn/current/Manual/class-ScriptableObject.html)
  * [日本語](/ja/current/Manual/class-ScriptableObject.html)
  * [한국어](/kr/current/Manual/class-ScriptableObject.html)

  * [Scripting](scripting.html)
  * [Get started with scripting](scripting-get-started.html)
  * [Fundamental Unity types](fundamental-unity-types.html)
  * ScriptableObject

[](class-MonoBehaviour.html)

MonoBehaviour

[](scripting-transform.html)

Transform

# ScriptableObject

[Switch to Scripting](../ScriptReference/ScriptableObject.html "Go to
ScriptableObject page in the Scripting Reference")

A ScriptableObject is a data container that you can use to save large amounts
of data, independent of class instances. One of the main use cases for
ScriptableObjects is to reduce your project’s memory usage by avoiding copies
of values. This is useful if your project has a **prefab** An asset type that
allows you to store a GameObject complete with components and properties. The
prefab acts as a template from which you can create new object instances in
the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) that stores unchanging data in
attached MonoBehaviour **scripts** A piece of code that allows you to create
your own Components, trigger game events, modify Component properties over
time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts).

Every time you instantiate that prefab, it will get its own copy of that data.
Instead of using this method and storing duplicated data, you can use a
ScriptableObject to store the data and then access it by reference from all
the prefabs. This means that there is one copy of the data in memory.

Just like MonoBehaviours, ScriptableObjects derive from the base
`UnityEngine.Object` but, unlike MonoBehaviours, you can’t attach a
ScriptableObject to a [GameObject](class-GameObject.html)The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject). Instead, you need to save them as
Assets in your Project.

When you use the Unity Editor, you can save data to ScriptableObjects while
editing and at runtime because ScriptableObjects use the Editor namespace and
Editor scripting. In a deployed build, however, you can’t use
ScriptableObjects to save data, but you can use the saved data from the
ScriptableObject Assets that you set up during development.

When you save data from Editor Tools to ScriptableObjects as an asset, Unity
writes the data to disk and it persists between sessions.

This page provides an overview of the ScriptableObject class and its common
uses when scripting with it. For a complete reference of every member of the
ScriptableObject class, refer to the [ScriptableObject script
reference](../ScriptReference/ScriptableObject.html).

## Using a ScriptableObject

The main use cases for ScriptableObjects are:

  * Saving and storing data during an Editor session
  * Saving data as an Asset in your Project to use at runtime

A ScriptableObject must inherit from the
[ScriptableObject](../ScriptReference/ScriptableObject.html) class.

To create a new ScriptableObject script, do one of the following:

  * In the main menu, go to **Assets** > **Create** > **Scripting** > and select **ScriptableObject Script**.
  * In the [Project window toolbar](ProjectView.html), right-click to open the Project window context menu, then select **Create** > **Scripting** > **ScriptableObject Script**. You can also click the plus sign in the Project Window to open the **Create** menu directly.

You can use the
[CreateAssetMenu](../ScriptReference/CreateAssetMenuAttribute.html) attribute
to create custom assets using your class. For example:

    
    
    using UnityEngine;
    
    [CreateAssetMenu(fileName = "Data", menuName = "ScriptableObjects/SpawnManagerScriptableObject", order = 1)]
    public class SpawnManagerScriptableObject : ScriptableObject
    {
        public string prefabName;
    
        public int numberOfPrefabsToCreate;
        public Vector3[] spawnPoints;
    }
    

With the previous script in your **Assets** Any media or data that can be used
in your game or project. An asset may come from a file created outside of
Unity, such as a 3D Model, an audio file or an image. You can also create some
asset types in Unity, such as an Animator Controller, an Audio Mixer or a
Render Texture. [More info](AssetWorkflow.html)  
See in [Glossary](Glossary.html#Asset) folder, you can create an instance of
your ScriptableObject by navigating to **Assets > Create > ScriptableObjects >
SpawnManagerScriptableObject**. Give your new ScriptableObject instance a
meaningful name and alter the values. To use these values, you need to create
a new script that references your ScriptableObject, in this case, a
`SpawnManagerScriptableObject`. For example:

    
    
    using UnityEngine;
    
    public class Spawner : MonoBehaviour
    {
        // The GameObject to instantiate.
        public GameObject entityToSpawn;
    
        // An instance of the ScriptableObject defined above.
        public SpawnManagerScriptableObject spawnManagerValues;
    
        // This will be appended to the name of the created entities and increment when each is created.
        int instanceNumber = 1;
    
        void Start()
        {
            SpawnEntities();
        }
    
        void SpawnEntities()
        {
            int currentSpawnPointIndex = 0;
    
            for (int i = 0; i < spawnManagerValues.numberOfPrefabsToCreate; i++)
            {
                // Creates an instance of the prefab at the current spawn point.
                GameObject currentEntity = Instantiate(entityToSpawn, spawnManagerValues.spawnPoints[currentSpawnPointIndex], Quaternion.identity);
    
                // Sets the name of the instantiated entity to be the string defined in the ScriptableObject and then appends it with a unique number. 
                currentEntity.name = spawnManagerValues.prefabName + instanceNumber;
    
                // Moves to the next spawn point index. If it goes out of range, it wraps back to the start.
                currentSpawnPointIndex = (currentSpawnPointIndex + 1) % spawnManagerValues.spawnPoints.Length;
    
                instanceNumber++;
            }
        }
    }
    

> **Note:** The script file must have the same name as the class.

Attach the previous script to a GameObject in your
[Scene](CreatingScenes.html)A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). Then, in the **Inspector** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), set the **Spawn Manager Values**
field to the new `SpawnManagerScriptableObject` that you set up.

Set the **Entity To Spawn** field to any prefab in your Assets folder, then
click **Play** in the Editor. The prefab you referenced in the `Spawner`
instantiates using the values you set in the `SpawnManagerScriptableObject`
instance.

If you’re working with ScriptableObject references in the Inspector, you can
double click the reference field to open the Inspector for your
ScriptableObject. You can also create a custom Editor to define the look of
the Inspector for your type to help manage the data that it represents.

## Additional resources

  * [ScriptableObject API reference](../ScriptReference/ScriptableObject.html)
  * [Introduction to ScriptableObjects](https://learn.unity.com/tutorial/introduction-to-scriptable-objects)

[](class-MonoBehaviour.html)

MonoBehaviour

[](scripting-transform.html)

Transform

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

