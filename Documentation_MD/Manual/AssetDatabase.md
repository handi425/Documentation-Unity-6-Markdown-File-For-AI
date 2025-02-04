[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AssetDatabase.html)
  * [中文](/cn/current/Manual/AssetDatabase.html)
  * [日本語](/ja/current/Manual/AssetDatabase.html)
  * [한국어](/kr/current/Manual/AssetDatabase.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AssetDatabase.html)
  * [中文](/cn/current/Manual/AssetDatabase.html)
  * [日本語](/ja/current/Manual/AssetDatabase.html)
  * [한국어](/kr/current/Manual/AssetDatabase.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * The Asset Database

[](AssetMetadata.html)

Asset Metadata

[](AssetDatabaseRefreshing.html)

Refreshing the Asset Database

# The Asset Database

With most types of asset, Unity needs to convert the data from the asset’s
source file into a format that it can use in a game or real-time application.
It stores these converted files, and the data associated with them, in the
**Asset Database**.

The conversion process is required because most file formats are optimized to
save storage space, whereas in a game or a real-time application, the asset
data needs to be in a format that is ready for hardware, such as the CPU,
graphics, or audio hardware, to use immediately. For example, when Unity
imports a .png image file as a texture, it does not use the original .png-
formatted data at runtime. Instead, when you import the texture, Unity creates
a new representation of the image in a different format which is stored in the
Project’s _Library_ folder. The Texture class in the Unity engine uses this
imported version, and Unity uploads it to the GPU for real-time display.

If you subsequently modify an asset’s source file that you have already
imported (or if you change any of its dependencies) Unity reimports the file
and updates the imported version of the data. See [Refreshing the Asset
Database](AssetDatabaseRefreshing.html) for more information on this process.

The Asset Database also provides an [AssetDatabase
API](../ScriptReference/AssetDatabase.html) that you can use to access Assets,
and control or customize the import process.

## Asset import dependencies

The Asset Database keeps track of all the dependencies for each asset, and
keeps a cache of the imported versions of all the Assets.

An asset’s import dependencies include all the data that might influence the
imported data. For example, the asset’s source file, the import settings of
the asset such as, a texture’s **compression** A method of storing data that
reduces the amount of storage space it requires. See [Texture
Compression](class-TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) type, or the target platform of
your project are dependencies. If you modify any of these dependencies, the
cached version of the imported asset becomes invalid and Unity must re-import
it to reflect the changes.

## Asset caching

The Asset Cache is where Unity stores the imported versions of assets. Because
Unity can always recreate these imported versions from the source asset file
and its dependencies, these imported versions are treated as a cache of pre-
calculated data, which saves time when you use Unity. For this reason, you
should exclude the files in the Asset Cache from **version control** A system
for managing file changes. You can use Unity in conjunction with most common
version control tools, including Perforce, Git, Mercurial and PlasticSCM.
[More info](VersionControl.html)  
See in [Glossary](Glossary.html#VersionControl) systems.

Unity uses a local cache by default, which means that the imported versions of
Assets are cached in the _Library_ folder in your Project’s folder on your
local machine. You should use an **ignore file** A special file used in many
Version Control Systems which specifies files to be excluded from being placed
under version control. In Unity projects there are a number of files which
could be excluded from version control, and using an Ignore File is the best
way to achieve this.  
See in [Glossary](Glossary.html#Ignorefile) to exclude this folder from
version control.

However, if you work as part of a team and use a version control system, it
might be beneficial to also use [Unity Accelerator](UnityAccelerator.html),
which shares the Asset Cache across your LAN.

Because cached Assets are not suitable for storing in a version control
system, when your team works together on a Project and uses local caching,
every team member’s copy of Unity performs the import process if an Asset or
dependency changes, which can be time consuming.

Unity provides a solution to this called [Unity
Accelerator](UnityAccelerator.html). One of the **Accelerator** The Unity
Accelerator is an external tool that provides an asset cache that keeps copies
of a team’s imported assets. The goal of the Accelerator is to speed up
teamwork and reduce iteration time by coordinating asset sharing so that you
don’t need to reimport portions of your project. [More
info](UnityAccelerator.html)  
See in [Glossary](Glossary.html#Accelerator)’s features is a software agent
which stores and serves the cached versions of Assets to everyone who is
working on the same Project together on the same local network. This means
that only one team member needs to import any given asset. The imported
version of the Asset is then stored in the Accelerator and the other team
members can download the cached version instead of waiting for the import
process locally.

## Source Assets and Artifacts

Unity maintains two database files in the Library folder, which together are
called the Asset Database. These two databases keep track of information about
your source asset files, and Artifacts, which is information about the import
results.

### The source Asset Database

The source Asset Database contains meta-information about your source asset
files which Unity uses to determine whether the file has been modified, and
therefore whether it should reimport the files. This includes information such
as last modified date, a hash of the file’s contents, GUIDs and other meta-
information.

### The Artifact database

Artifacts are the results of the import process. The Artifact database
contains information about the import results of each source asset. Each
Artifact contains the import dependency information, Artifact meta-information
and a list of Artifact files.

**Note:** The database files are located in your Project’s _Library_ folder,
and as such you should exclude them from version control systems. You can find
them in the following locations:

  * Source Asset Database: `Library\SourceAssetDB`
  * Artifact Database: `Library\ArtifactDB`

## Importing an Asset

Unity normally imports assets automatically when they are dragged into the
project but it is also possible to import them under script control. To do
this you can use the
[AssetDatabase.ImportAsset](../ScriptReference/AssetDatabase.ImportAsset.html)
method as in the example below.

    
    
    using UnityEngine;
    using UnityEditor;
    
    public class ImportAsset {
        [MenuItem ("AssetDatabase/ImportExample")]
        static void ImportExample ()
        {
            AssetDatabase.ImportAsset("Assets/Textures/texture.jpg", ImportAssetOptions.Default);
        }
    }
    
    

You can also pass an extra parameter of type
[AssetDatabase.ImportAssetOptions](../ScriptReference/ImportAssetOptions.html)
to the AssetDatabase.ImportAsset call. The scripting reference page documents
the different options and their effects on the function’s behaviour.

## Loading an Asset

The editor loads assets only as needed, say if they are added to the **scene**
A Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) or edited from the **Inspector** A
Unity window that displays information about the currently selected
GameObject, asset or project settings, allowing you to inspect and edit the
values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) panel. However, you can load and
access assets from a script using
[AssetDatabase.LoadAssetAtPath](../ScriptReference/AssetDatabase.LoadAssetAtPath.html),
[AssetDatabase.LoadMainAssetAtPath](../ScriptReference/AssetDatabase.LoadMainAssetAtPath.html),
[AssetDatabase.LoadAllAssetRepresentationsAtPath](../ScriptReference/AssetDatabase.LoadAllAssetRepresentationsAtPath.html)
and
[AssetDatabase.LoadAllAssetsAtPath](../ScriptReference/AssetDatabase.LoadAllAssetsAtPath.html).
See the scripting documentation for further details.

    
    
    using UnityEngine;
    using UnityEditor;
    
    public class ImportAsset {
        [MenuItem ("AssetDatabase/LoadAssetExample")]
        static void ImportExample ()
        {
            Texture2D t = AssetDatabase.LoadAssetAtPath("Assets/Textures/texture.jpg", typeof(Texture2D)) as Texture2D;
        }
    }
    
    

## File Operations using the AssetDatabase

Since Unity keeps metadata about asset files, you should never create, move or
delete them using the filesystem. Instead, you can use
[AssetDatabase.Contains](../ScriptReference/AssetDatabase.Contains.html),
[AssetDatabase.CreateAsset](../ScriptReference/AssetDatabase.CreateAsset.html),
[AssetDatabase.CreateFolder](../ScriptReference/AssetDatabase.CreateFolder.html),
[AssetDatabase.RenameAsset](../ScriptReference/AssetDatabase.RenameAsset.html),
[AssetDatabase.CopyAsset](../ScriptReference/AssetDatabase.CopyAsset.html),
[AssetDatabase.MoveAsset](../ScriptReference/AssetDatabase.MoveAsset.html),
[AssetDatabase.MoveAssetToTrash](../ScriptReference/AssetDatabase.MoveAssetToTrash.html)
and
[AssetDatabase.DeleteAsset](../ScriptReference/AssetDatabase.DeleteAsset.html).

    
    
    public class AssetDatabaseIOExample {
        [MenuItem ("AssetDatabase/FileOperationsExample")]
        static void Example ()
        {
            string ret;
            
            // Create
            Material material = new Material (Shader.Find("Specular"));
            AssetDatabase.CreateAsset(material, "Assets/MyMaterial.mat");
            if(AssetDatabase.Contains(material))
                Debug.Log("Material asset created");
            
            // Rename
            ret = AssetDatabase.RenameAsset("Assets/MyMaterial.mat", "MyMaterialNew");
            if(ret == "")
                Debug.Log("Material asset renamed to MyMaterialNew");
            else
                Debug.Log(ret);
            
            // Create a Folder
            ret = AssetDatabase.CreateFolder("Assets", "NewFolder");
            if(AssetDatabase.GUIDToAssetPath(ret) != "")
                Debug.Log("Folder asset created");
            else
                Debug.Log("Couldn't find the GUID for the path");
            
            // Move
            ret = AssetDatabase.MoveAsset(AssetDatabase.GetAssetPath(material), "Assets/NewFolder/MyMaterialNew.mat");
            if(ret == "")
                Debug.Log("Material asset moved to NewFolder/MyMaterialNew.mat");
            else
                Debug.Log(ret);
            
            // Copy
            if(AssetDatabase.CopyAsset(AssetDatabase.GetAssetPath(material), "Assets/MyMaterialNew.mat"))
                Debug.Log("Material asset copied as Assets/MyMaterialNew.mat");
            else
                Debug.Log("Couldn't copy the material");
            // Manually refresh the Database to inform of a change
            AssetDatabase.Refresh();
            Material MaterialCopy = AssetDatabase.LoadAssetAtPath("Assets/MyMaterialNew.mat", typeof(Material)) as Material;
            
            // Move to Trash
            if(AssetDatabase.MoveAssetToTrash(AssetDatabase.GetAssetPath(MaterialCopy)))
                Debug.Log("MaterialCopy asset moved to trash");
            
            // Delete
            if(AssetDatabase.DeleteAsset(AssetDatabase.GetAssetPath(material)))
                Debug.Log("Material asset deleted");
            if(AssetDatabase.DeleteAsset("Assets/NewFolder"))
                Debug.Log("NewFolder deleted");
            
            // Refresh the AssetDatabase after all the changes
            AssetDatabase.Refresh();
        }
    }
    
    

## Platform Switching and reimporting

Switching between platforms might cause Unity to reimport your assets. This
usually happens when the way the asset is imported differs between platforms,
which is often the case. For example, different platforms have different
**texture formats** A file format for handling textures during real-time
rendering by 3D graphics hardware, such as a graphics card or mobile device.
[More info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureFormat), so textures are imported
differently for each platform.

When using Asset Database V2, the platform is part of the hash that the Asset
Database uses to store the import results for Unity’s built-in importers. This
means that the results for importing your assets on different platforms are
stored as separate pieces of cached data.

The result of this feature is that the first time you switch platform with new
assets in your project that haven’t already been imported for that platform,
they are reimported. This means that you have to wait for that process to
complete. However the new reimported data does not overwrite the old data
cached import for the previous platform.

This means whenever you subsequently switch back to a platform where you have
already imported assets for that platform, those asset import results are
already cached and ready to use, making the switch much faster.

## Asset Database version

This documentation refers to the **version 2** of the Asset Database, which is
the default in new Projects created with Unity 2019.3 or newer. The legacy
version (version 1) was the default in earlier versions of Unity, which
behaves in a different way. The legacy version cannot be used in Unity 2020+.

[](AssetMetadata.html)

Asset Metadata

[](AssetDatabaseRefreshing.html)

Refreshing the Asset Database

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

