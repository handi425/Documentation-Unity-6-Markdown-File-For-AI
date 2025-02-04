[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ScriptedImporters.html)
  * [中文](/cn/current/Manual/ScriptedImporters.html)
  * [日本語](/ja/current/Manual/ScriptedImporters.html)
  * [한국어](/kr/current/Manual/ScriptedImporters.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ScriptedImporters.html)
  * [中文](/cn/current/Manual/ScriptedImporters.html)
  * [日本語](/ja/current/Manual/ScriptedImporters.html)
  * [한국어](/kr/current/Manual/ScriptedImporters.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [Supported Asset Types](AssetTypes.html)
  * Scripted Importers

[](BuiltInImporters.html)

Built-in Importers

[](ImporterConsistency.html)

Importer Consistency

## Scripted Importers

Scripted Importers are part of the [Unity Scripting API](scripting.html). You
can use Scripted Importers to write custom Asset importers in C#, which allows
you to add your own support for file formats that are not natively supported
by Unity.

You can create a custom importer by specializing the abstract class
[ScriptedImporter](../ScriptReference/AssetImporters.ScriptedImporter.html)
and applying the
[ScriptedImporter](../ScriptReference/AssetImporters.ScriptedImporterAttribute.html)
attribute. This registers your custom importer to handle one or more file
extensions. When a file matching the registered file extensions is detected by
the Asset pipeline as being new or changed, Unity invokes the method
`OnImportAsset` of your custom importer.

_Note: Scripted Importers cannot handle a file extension that is already
natively handled by Unity._

### Example

Below is a simple example as Scripted Importer: It imports asset files with
the extension “cube” into a Unity **Prefab** An asset type that allows you to
store a GameObject complete with components and properties. The prefab acts as
a template from which you can create new object instances in the scene. [More
info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) with a cube primitive as the main
Asset and a default material and color, and assigns its position from a value
read from the Asset file:

    
    
    using UnityEngine;
    using UnityEditor.AssetImporters;
    using System.IO;
    
    [ScriptedImporter(1, "cube")]
    public class CubeImporter : ScriptedImporter
    {
        public float m_Scale = 1;
    
        public override void OnImportAsset(AssetImportContext ctx)
        {
            var cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
            var position = JsonUtility.FromJson<Vector3>(File.ReadAllText(ctx.assetPath));
    
            cube.transform.position = position;
            cube.transform.localScale = new Vector3(m_Scale, m_Scale, m_Scale);
    
            // 'cube' is a GameObject and will be automatically converted into a prefab
            // (Only the 'Main Asset' is eligible to become a Prefab.)
            ctx.AddObjectToAsset("main obj", cube);
            ctx.SetMainObject(cube);
    
            var material = new Material(Shader.Find("Standard"));
            material.color = Color.red;
    
            // Assets must be assigned a unique identifier string consistent across imports
            ctx.AddObjectToAsset("my Material", material);
    
            // Assets that are not passed into the context as import outputs must be destroyed
            var tempMesh = new Mesh();
            DestroyImmediate(tempMesh);
        }
    }
    

**Note** :

  * The importer is registered with Unity’s Asset pipeline by placing the `ScriptedImporter` attribute on the CubeImporter class.
  * The CubeImporter class implements the abstract `ScriptedImporter` base class.
  * `OnImportAsset`’s ctx argument contains both input and output data for the import event.
  * Each import event must generate one (and only one) call to `SetMainAsset`.
  * Each import event may generate as many calls to `AddSubAsset` as necessary.
  * Please refer to the [Scripting API documentation](../ScriptReference/AssetImporters.ScriptedImporter.html) for more details.

You may also implement a custom Import Settings Editor by specializing
[ScriptedImporterEditor](../ScriptReference/AssetImporters.ScriptedImporterEditor.html)
class and decorating it with the class attribute `CustomEditor` to tell it
what type of importer it is used for.

For example:

    
    
    using UnityEditor;
    using UnityEditor.AssetImporters;
    using UnityEditor.SceneManagement;
    using UnityEngine;
    
    [CustomEditor(typeof(CubeImporter))]
    public class CubeImporterEditor: ScriptedImporterEditor
    {
        public override void OnInspectorGUI()
        {
            var colorShift = new GUIContent("Color Shift");
            var prop = serializedObject.FindProperty("m_ColorShift");
            EditorGUILayout.PropertyField(prop, colorShift);
            base.ApplyRevertGUI();
        }
    }
    

### Using a Scripted Importer

Once you have added a scripted importer class to a project, you may use it
just like any other native file type supported by Unity:

  * Drop a supported file in the Asset directory hierarchy to import.
  * Restarting the Unity Editor reimports any files that have changed since last update.
  * Editing the Asset file on disk and returning to the Unity Editor triggers a reimport.
  * Import a new asset using **Asset** Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](AssetWorkflow.html)  
See in [Glossary](Glossary.html#Asset) > **Import New Asset…**.

  * Explicitly trigger a re-import via the menu: **Asset** > **Reimport**.
  * Click on the Asset to see its settings in the [Inspector window](UsingTheInspector.html). To modify its settings, edit them in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window and click **Apply** .  
  

![The Inspector window of an Asset \(An Alembic Girl\) imported by the
Scripted Importer](../uploads/Main/ScriptedImporters-2.png) The Inspector
window of an Asset (An Alembic Girl) imported by the Scripted Importer

### Real-world use of Scripted Importers

  * **Alembic** : The Alembic importer **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) has been updated to use a Scripted
Importer. For more information, visit [Unity github:
AlembicImporter](https://github.com/unity3d-jp/AlembicImporter).

  * **USD** : The USD importer plug-in uses a Scripted Importer. For more information, refer to the [USD Importer package documentation](https://docs.unity3d.com/Packages/com.unity.importer.usd@1.0/manual/index.html).

[](BuiltInImporters.html)

Built-in Importers

[](ImporterConsistency.html)

Importer Consistency

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

