[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/FormatDescription.html)
  * [中文](/cn/current/Manual/FormatDescription.html)
  * [日本語](/ja/current/Manual/FormatDescription.html)
  * [한국어](/kr/current/Manual/FormatDescription.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/FormatDescription.html)
  * [中文](/cn/current/Manual/FormatDescription.html)
  * [日本語](/ja/current/Manual/FormatDescription.html)
  * [한국어](/kr/current/Manual/FormatDescription.html)

  * [The Unity Editor](unity-editor.html)
  * [Editor Features](EditorFeatures.html)
  * [Text-Based Scene Files](TextSceneFormat.html)
  * Format of Text Serialized files

[](TextSceneFormat.html)

Text-Based Scene Files

[](UnityYAML.html)

UnityYAML

# Format of Text Serialized files

Unity’s **Scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) format uses a custom subset of the YAML
data serialization language. YAML is an open format with documentation about
it available on the [YAML website](http://yaml.org/spec/1.2/spec.html). For
more information about the YAML used in unity, read the documentation on
[UnityYAML](UnityYAML.html).

The file writes each Object in a Scene as a separate YAML document. The `---`
sequence introduces each Object in the file. In this context, the term
“Object” refers to **GameObjects** The fundamental object in Unity scenes,
which can represent characters, props, scenery, cameras, waypoints, and more.
A GameObject’s functionality is defined by the Components attached to it.
[More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), Components and other scene data
collectively: each of these items needs its own YAML document in the scene
file. The following example shows the basic structure of a serialized object:

    
    
    --- !u!1 &6
    GameObject:
      m_ObjectHideFlags: 0
      m_PrefabParentObject: {fileID: 0}
      m_PrefabInternal: {fileID: 0}
      importerVersion: 3
      m_Component:
      - 4: {fileID: 8}
      - 33: {fileID: 12}
      - 65: {fileID: 13}
      - 23: {fileID: 11}
      m_Layer: 0
      m_Name: Cube
      m_TagString: Untagged
      m_Icon: {fileID: 0}
      m_NavMeshLayer: 0
      m_StaticEditorFlags: 0
      m_IsActive: 1
    
    

The first line contains the string `!u!1 &6` after the document marker. The
first number after `!u!` indicates the class of the object (in this case, it
is a GameObject). The number following the ampersand is an object ID number
unique within the file, although the number is assigned to each object
arbitrarily. Each of the object’s serializable properties is denoted by a line
like the following:

    
    
    m_Name: Cube
    

Properties are typically prefixed with `m_` but otherwise follow the name of
the property as defined in the script reference. The following example shows
how a second object, defined further down in the file looks:

    
    
    --- !u!4 &8
    Transform:
      m_ObjectHideFlags: 0
      m_PrefabParentObject: {fileID: 0}
      m_PrefabInternal: {fileID: 0}
      m_GameObject: {fileID: 6}
      m_LocalRotation: {x: 0.000000, y: 0.000000, z: 0.000000, w: 1.000000}
      m_LocalPosition: {x: -2.618721, y: 1.028581, z: 1.131627}
      m_LocalScale: {x: 1.000000, y: 1.000000, z: 1.000000}
      m_Children: []
      m_Father: {fileID: 0}
    
    

The following example shows an attached **Transform component** A Transform
component determines the Position, Rotation, and Scale of each object in the
scene. Every GameObject has a Transform. [More info](class-Transform.html)  
See in [Glossary](Glossary.html#TransformComponent) to the GameObject defined
by the YAML document above. `{fileID:6}` is used to represent the GameObject
as the GameObject’s object ID within the file was 6.

    
    
    m_GameObject: {fileID: 6}
    

…

Decimal representation or hexadecimal numbers in IEEE 754 format (denoted by a
0x prefix) can be used to represent floating point numbers. Unity uses the
IEEE 754 representation for lossless encoding of values and to write floating
point values which don’t have a short decimal representation. When Unity
writes numbers in hexadecimal, it always writes the decimal format in
parentheses for debugging purposes, but only the hex is actually parsed when
loading the file. To edit these values manually, remove the hex and enter a
decimal number. The following example shows a valid representation of floating
point values (all representing the number one):

    
    
    myValue: 0x3F800000
    myValue: 1
    myValue: 1.000
    myValue: 0x3f800000(1)
    myValue: 0.1e1
    
    

* * *

  * 2018–05–13 Page published 

[](TextSceneFormat.html)

Text-Based Scene Files

[](UnityYAML.html)

UnityYAML

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

