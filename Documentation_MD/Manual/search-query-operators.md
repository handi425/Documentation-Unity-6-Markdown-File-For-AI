[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/search-query-operators.html)
  * [中文](/cn/current/Manual/search-query-operators.html)
  * [日本語](/ja/current/Manual/search-query-operators.html)
  * [한국어](/kr/current/Manual/search-query-operators.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/search-query-operators.html)
  * [中文](/cn/current/Manual/search-query-operators.html)
  * [日本語](/ja/current/Manual/search-query-operators.html)
  * [한국어](/kr/current/Manual/search-query-operators.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity Search](search-overview.html)
  * [Search usage](search-usage.html)
  * Search query operators

[](search-filters.html)

Filter searches

[](search-index-manager.html)

The Index Manager

# Search query operators

Most Search Providers use a
[`QueryEngine`](../ScriptReference/Search.QueryEngine.html) (SceneA Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), AssetAny media or data that can be
used in your game or project. An asset may come from a file created outside of
Unity, such as a 3D Model, an audio file or an image. You can also create some
asset types in Unity, such as an Animator Controller, an Audio Mixer or a
Render Texture. [More info](AssetWorkflow.html)  
See in [Glossary](Glossary.html#Asset), ObjectsThe fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#Object) and Resource providers) to parse and
resolve their queries. They support a basic set of Query Operators that allow
for more complex queries using Boolean operators and parentheses grouping. The
table on this page lists the supported Query Operators.

**Case sensitivity** : Most Search queries ignore case. For example, `Stone`
or `stone` or `sToNe` will yield the same results.

**Filter** | **Search token** | **Description**  
---|---|---  
**Basic search** | `<any partial name>` |  `main`  
Searches matching the word `Main`  
**And** | `and` |  `Main and t:camera`  
Search where name contains `Main` and is of type name containing `camera`  
  
`t:texture and jpg`  
Searches all of type `texture` containing `jpg` in their filename.  
  
Note: Since `and` **is the default operator of the QueryEngine** the last
query is equivalent to:  
`t:texture jpg`  
**or** | `or` |  `Player or Monster`  
Searches containing the word `Player` or `Monster`.  
**Group** | `(<group content>)` |  `t:Character and (status=Poison or status=Stunned)`  
Searches for a `Character` component where the value of `status` property is
either `Poison` or `Stunned`.  
**Exclusion** | `-<Expression to exclude>` |  `p: dep:door -t:Scene`  
Searches all Assets with a dependency on an Asset containing the word `door`
and that are not of type `Scene`.  
  
`p: dep:door -stone`  
Searches all Assets with a dependency on an Asset containing the word `door`
and that do not contain the word `stone`.  
**Exact Operator** | `!<something>` | Most of the string matching in Search returns partial matches. Use the `!` operator to return **exact** matches.  
  
`p: stone`  
Searches all Assets containing the word stone (`stone_hammer.png`,
`stone_door.prefab`).  
  
`p: !stone`  
Searches all Assets with the exact name `stone` (e.g.: `stone.png`)  
**Partial Value match (:)** | `property:<partial value>` |  `ref:aster`  
Because `:` is used, searches all Assets having an Asset containing the word
`aster` (ex: `asteroid2`, `asteroids`) as a dependency.  
**Exact Value (=)** | `property=exactValue` |  `ref=asteroid`  
Because `=` is used, searches all Assets having an Asset with the exact name
`asteroid` as a dependency.  
**>** | `property>number` |  `t:texture size>256`  
Searches all textures with a size bigger than 256 bytes.  
**<** | `property<number` |  `t:texture size<256`  
Searches all textures with a size smaller than 256 bytes.  
**!=** | `property!=number` |  `t:texture size!=256`  
Searches all textures with a size different than 256 bytes.  
**> =** | `property>=number` |  `t:texture size>=256`  
Searches all textures with a size bigger or equal than 256 bytes.  
**< =** | `property>number` |  `t:texture size<=256`  
Searches all textures with a size smaller or equal than 256 bytes.  
  
[](search-filters.html)

Filter searches

[](search-index-manager.html)

The Index Manager

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

