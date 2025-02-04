[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/Archives.html)
  * [中文](/cn/current/Manual/Archives.html)
  * [日本語](/ja/current/Manual/Archives.html)
  * [한국어](/kr/current/Manual/Archives.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/Archives.html)
  * [中文](/cn/current/Manual/Archives.html)
  * [日本語](/ja/current/Manual/Archives.html)
  * [한국어](/kr/current/Manual/Archives.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * Archives

[](upm-ui-remove-local.html)

Removing local asset packages

[](assets-optimizing.html)

Optimizing assets

# Archives

The Unity **archive** file format is a generic packaging format which can
store any type of file, similar to a .zip file.

This file format is used by AssetBundles. The AssetBundle archive files are
created as a final stage of the build process, e.g.
[BuildPipeline.BuildAssetBundles](../ScriptReference/BuildPipeline.BuildAssetBundles.html).
They are mounted into the Unity virtual file system when the AssetBundle is
loaded, e.g.
[AssetBundle.LoadFromFile](../ScriptReference/AssetBundle.LoadFromFile.html).

This file format is also used for Player content when the Player is built with
[BuildOptions.CompressWithLz4](../ScriptReference/BuildOptions.CompressWithLz4.html).
In that case the Archive is mounted automatically when the player runs.

This section describes lower-level APIs that Unity provides for working with
archives.

## Archive File System

The
[ArchiveFileInterface](../ScriptReference/Unity.IO.Archive.ArchiveFileInterface.html)
API can be use to load archives. They are mounted into a
[Unity.Content.ContentNamespace](../ScriptReference/Unity.Content.ContentNamespace.html).
Once Unity mounts the file, your application can access the files inside an
Archive through any Unity systems that use Unity’s virtual file system. Use
the
[AsyncReadManager](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManager.html)
to access the virtual file system directly.

## Create and mount an archive

The following example describes how to create an archive with the
[ContentBuildInterface.ArchiveAndCompress](../ScriptReference/Build.Content.ContentBuildInterface.ArchiveAndCompress.html)
function and mount the archive with the
[ArchiveFileInterface.MountAsync](../ScriptReference/Unity.IO.Archive.ArchiveFileInterface.MountAsync.html)
function. This example produces an archive that uses LZ4 **compression** A
method of storing data that reduces the amount of storage space it requires.
See [Texture Compression](class-TextureImporterOverride), [Animation
Compression](class-AnimationClip.html#AssetProperties), [Audio
Compression](class-AudioClip.html), [Build
Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) and contains one text file.

    
    
    using Unity.Collections.LowLevel.Unsafe;
    using Unity.Content;
    using Unity.IO.Archive;
    using Unity.IO.LowLevel.Unsafe;
    using UnityEngine;
    #if UNITY_EDITOR
    using UnityEditor.Build.Content;
    #endif
    
    public class SampleBehaviour : MonoBehaviour
    {
    #if UNITY_EDITOR
      unsafe void CreateAndMountArchive()
      { 
        // Create the Archive
        ResourceFile[] rFiles = new ResourceFile[1];
        ResourceFile rf = new ResourceFile();
        rf.fileName = "Assets/file1.txt"; // Path of the existing file, to copy into the Archive
        rf.fileAlias = "file1.txt";       // Path given to the file inside the Archive
        rFiles[0] = rf;
    
        string archivePath = System.IO.Path.Combine(Application.streamingAssetsPath, "myArchive");
        ContentBuildInterface.ArchiveAndCompress(rFiles, archivePath, UnityEngine.BuildCompression.LZ4);
    
        // Mount the Archive
        var ns = ContentNamespace.GetOrCreateNamespace("MyNamespace123");
        ArchiveHandle ahandle = ArchiveFileInterface.MountAsync(ns, archivePath, "a:");
        ahandle.JobHandle.Complete();
    
        string textFilePath = ahandle.GetMountPath() + "file1.txt"; // ns:/MyNamespace123/a:/file1.txt
        ReadCommand cmd;
        cmd.Size = 1024;
        cmd.Buffer = UnsafeUtility.Malloc(cmd.Size, 4, Unity.Collections.Allocator.Temp);
        cmd.Offset = 0;
        
        NativeArray<ReadCommand> cmds = new NativeArray<ReadCommand>(1, Allocator.Persistent);
        cmds[0] = cmd;
    
        ReadHandle rHandle = AsyncReadManager.Read(textFilePath, (ReadCommand*)cmds.GetUnsafePtr(), 1);
        rHandle.JobHandle.Complete();
    
        // ...At this point cmd.Buffer contains contents from file1.txt (up to 1024 bytes)...
    
        rHandle.Dispose();
        UnsafeUtility.Free(cmd.Buffer, Unity.Collections.Allocator.Temp);
        cmds.Dipose():
    
        ahandle.Unmount().Complete();
      }
    #endif
    }
    

[](upm-ui-remove-local.html)

Removing local asset packages

[](assets-optimizing.html)

Optimizing assets

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

