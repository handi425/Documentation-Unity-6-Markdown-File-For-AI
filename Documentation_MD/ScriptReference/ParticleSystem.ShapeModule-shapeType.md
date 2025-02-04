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

#  [ParticleSystem.ShapeModule](ParticleSystem.ShapeModule.html).shapeType

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

[Switch to Manual](../Manual/class-ParticleSystem.html "Go to ParticleSystem
Component in the Manual")

public [ParticleSystemShapeType](ParticleSystemShapeType.html) shapeType;

### Description

The type of shape to emit particles from.

    
    
    using UnityEngine;
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections;
    using System.Collections.Generic;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public [ParticleSystemShapeType](ParticleSystemShapeType.html) shapeType = [ParticleSystemShapeType.Cone](ParticleSystemShapeType.Cone.html);
        private int shapeTypeIndex = 2;
        public float arc = 360.0f;
        public [ParticleSystemShapeMultiModeValue](ParticleSystemShapeMultiModeValue.html) arcMode = [ParticleSystemShapeMultiModeValue.Random](ParticleSystemShapeMultiModeValue.Random.html);
        public float arcSpread = 0.0f;
        public float arcSpeed = 1.0f;
        public float angle = 25.0f;
        public float radius = 1.0f;
        public float radiusThickness = 1.0f;
        public [ParticleSystemShapeMultiModeValue](ParticleSystemShapeMultiModeValue.html) radiusMode = [ParticleSystemShapeMultiModeValue.Random](ParticleSystemShapeMultiModeValue.Random.html);
        public float radiusSpread = 0.0f;
        public float radiusSpeed = 1.0f;
        public float donutRadius = 0.2f;
        public float length = 2.0f;
        public [Vector3](Vector3.html) boxThickness = new [Vector3](Vector3.html)(0.0f, 0.0f, 0.0f);
        public [ParticleSystemMeshShapeType](ParticleSystemMeshShapeType.html) meshShapeType;
        public float normalOffset = 0.0f;
        public float randomizeDirection = 0.0f;
        public float spherizeDirection = 0.0f;
        public float randomizePosition = 0.0f;
        public [Vector3](Vector3.html) position = new [Vector3](Vector3.html)(0.0f, 0.0f, 0.0f);
        public [Vector3](Vector3.html) rotation = new [Vector3](Vector3.html)(0.0f, 0.0f, 0.0f);
        public [Vector3](Vector3.html) scale = new [Vector3](Vector3.html)(1.0f, 1.0f, 1.0f);  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var main = ps.main;
            main.startSpeed = 0.1f;
            main.startSize = 0.1f;
            main.startLifetime = 1.0f;  
      
            var emission = ps.emission;
            emission.rateOverTime = 500.0f;  
      
            var shape = ps.shape;
            shape.mesh = Resources.GetBuiltinResource<[Mesh](Mesh.html)>("Capsule.fbx");
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var shape = ps.shape;
            shape.shapeType = shapeType;
            shape.arc = arc;
            shape.arcMode = arcMode;
            shape.arcSpread = arcSpread;
            shape.arcSpeed = arcSpeed;
            shape.angle = angle;
            shape.radius = radius;
            shape.radiusMode = radiusMode;
            shape.radiusSpread = radiusSpread;
            shape.radiusSpeed = radiusSpeed;
            shape.radiusThickness = radiusThickness;
            shape.donutRadius = donutRadius;
            shape.length = length;
            shape.boxThickness = boxThickness;
            shape.meshShapeType = meshShapeType;
            shape.normalOffset = normalOffset;
            shape.randomDirectionAmount = randomizeDirection;
            shape.sphericalDirectionAmount = spherizeDirection;
            shape.randomPositionAmount = randomizePosition;
            shape.position = position;
            shape.rotation = rotation;
            shape.scale = scale;
        }  
      
        void OnGUI()
        {
            List<[GUIContent](GUIContent.html)> content = new List<[GUIContent](GUIContent.html)>();
            for (int i = 0; i < (int)[ParticleSystemShapeType.SpriteRenderer](ParticleSystemShapeType.SpriteRenderer.html) + 1; i++)
            {
                [ParticleSystemShapeType](ParticleSystemShapeType.html) currentShapeType = ([ParticleSystemShapeType](ParticleSystemShapeType.html))i;
                var obsoleteAttribute = Attribute.GetCustomAttribute(currentShapeType.GetType().GetField(currentShapeType.ToString()), typeof(ObsoleteAttribute), false);   // skip the obsolete shape types
                if (obsoleteAttribute == null)
                    content.Add(new [GUIContent](GUIContent.html)(currentShapeType.ToString(), i.ToString()));
            }
            shapeTypeIndex = [GUI.SelectionGrid](GUI.SelectionGrid.html)(new [Rect](Rect.html)(25, 25, 1000, 80), shapeTypeIndex, content.ToArray(), content.Count / 3);
            shapeType = ([ParticleSystemShapeType](ParticleSystemShapeType.html))int.Parse(content[shapeTypeIndex].tooltip);  
      
            float y = 120.0f;
            float spacing = 40.0f;  
      
            if (shapeType == [ParticleSystemShapeType.Sphere](ParticleSystemShapeType.Sphere.html) || shapeType == [ParticleSystemShapeType.Hemisphere](ParticleSystemShapeType.Hemisphere.html))
            {
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Radius");
                radius = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), radius, 1.0f, 5.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Radius Thickness");
                radiusThickness = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), radiusThickness, 0.0f, 1.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc");
                arc = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), arc, 1.0f, 360.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc [Mode](Scripting.GarbageCollector.Mode.html)");
                arcMode = ([ParticleSystemShapeMultiModeValue](ParticleSystemShapeMultiModeValue.html))[GUI.SelectionGrid](GUI.SelectionGrid.html)(new [Rect](Rect.html)(165, 280, 360, 20), (int)arcMode, new [GUIContent](GUIContent.html)[] { new [GUIContent](GUIContent.html)("[Random](Random.html)"), new [GUIContent](GUIContent.html)("Loop"), new [GUIContent](GUIContent.html)("[Ping](Ping.html)-Pong"), new [GUIContent](GUIContent.html)("[Burst](ParticleSystem.Burst.html) Spread") }, 4);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc Spread");
                arcSpread = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), arcSpread, 0.0f, 1.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc Speed");
                arcSpeed = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), arcSpeed, 0.0f, 2.0f);
                y += spacing;
            }  
      
            if (shapeType == [ParticleSystemShapeType.Cone](ParticleSystemShapeType.Cone.html) || shapeType == [ParticleSystemShapeType.ConeVolume](ParticleSystemShapeType.ConeVolume.html))
            {
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "[Angle](UIElements.Angle.html)");
                angle = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), angle, 1.0f, 90.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Radius");
                radius = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), radius, 0.2f, 5.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Radius Thickness");
                radiusThickness = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), radiusThickness, 0.0f, 1.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc");
                arc = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), arc, 1.0f, 360.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc [Mode](Scripting.GarbageCollector.Mode.html)");
                arcMode = ([ParticleSystemShapeMultiModeValue](ParticleSystemShapeMultiModeValue.html))[GUI.SelectionGrid](GUI.SelectionGrid.html)(new [Rect](Rect.html)(165, 280, 360, 20), (int)arcMode, new [GUIContent](GUIContent.html)[] { new [GUIContent](GUIContent.html)("[Random](Random.html)"), new [GUIContent](GUIContent.html)("Loop"), new [GUIContent](GUIContent.html)("[Ping](Ping.html)-Pong"), new [GUIContent](GUIContent.html)("[Burst](ParticleSystem.Burst.html) Spread") }, 4);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc Spread");
                arcSpread = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), arcSpread, 0.0f, 1.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc Speed");
                arcSpeed = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), arcSpeed, 0.0f, 2.0f);
                y += spacing;  
      
                if (shapeType == [ParticleSystemShapeType.ConeVolume](ParticleSystemShapeType.ConeVolume.html))
                {
                    [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "[Length](UIElements.Length.html)");
                    length = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), length, 1.0f, 5.0f);
                    y += spacing;
                }
            }  
      
            if (shapeType == [ParticleSystemShapeType.Box](ParticleSystemShapeType.Box.html) || shapeType == [ParticleSystemShapeType.BoxShell](ParticleSystemShapeType.BoxShell.html) || shapeType == [ParticleSystemShapeType.BoxEdge](ParticleSystemShapeType.BoxEdge.html))
            {
                if (shapeType == [ParticleSystemShapeType.BoxShell](ParticleSystemShapeType.BoxShell.html) || shapeType == [ParticleSystemShapeType.BoxEdge](ParticleSystemShapeType.BoxEdge.html))
                {
                    [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "[Box](UIElements.Box.html) Thickness");
                    boxThickness.x = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 50, 30), boxThickness.x, 0.0f, 1.0f);
                    boxThickness.y = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(220, y + 5, 50, 30), boxThickness.y, 0.0f, 1.0f);
                    boxThickness.z = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(275, y + 5, 50, 30), boxThickness.z, 0.0f, 1.0f);
                    y += spacing;
                }
            }  
      
            if (shapeType == [ParticleSystemShapeType.Donut](ParticleSystemShapeType.Donut.html))
            {
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc");
                arc = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), arc, 1.0f, 360.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc [Mode](Scripting.GarbageCollector.Mode.html)");
                arcMode = ([ParticleSystemShapeMultiModeValue](ParticleSystemShapeMultiModeValue.html))[GUI.SelectionGrid](GUI.SelectionGrid.html)(new [Rect](Rect.html)(165, y, 360, 20), (int)arcMode, new [GUIContent](GUIContent.html)[] { new [GUIContent](GUIContent.html)("[Random](Random.html)"), new [GUIContent](GUIContent.html)("Loop"), new [GUIContent](GUIContent.html)("[Ping](Ping.html)-Pong"), new [GUIContent](GUIContent.html)("[Burst](ParticleSystem.Burst.html) Spread") }, 4);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc Spread");
                arcSpread = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), arcSpread, 0.0f, 1.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc Speed");
                arcSpeed = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), arcSpeed, 0.0f, 2.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Radius");
                radius = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), radius, 0.2f, 5.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Radius Thickness");
                radiusThickness = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), radiusThickness, 0.0f, 1.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Donut Radius");
                donutRadius = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), donutRadius, 0.0f, 5.0f);
                y += spacing;
            }  
      
            if (shapeType == [ParticleSystemShapeType.Circle](ParticleSystemShapeType.Circle.html))
            {
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc");
                arc = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), arc, 1.0f, 360.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc [Mode](Scripting.GarbageCollector.Mode.html)");
                arcMode = ([ParticleSystemShapeMultiModeValue](ParticleSystemShapeMultiModeValue.html))[GUI.SelectionGrid](GUI.SelectionGrid.html)(new [Rect](Rect.html)(165, y, 360, 20), (int)arcMode, new [GUIContent](GUIContent.html)[] { new [GUIContent](GUIContent.html)("[Random](Random.html)"), new [GUIContent](GUIContent.html)("Loop"), new [GUIContent](GUIContent.html)("[Ping](Ping.html)-Pong"), new [GUIContent](GUIContent.html)("[Burst](ParticleSystem.Burst.html) Spread") }, 4);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc Spread");
                arcSpread = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), arcSpread, 0.0f, 1.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Arc Speed");
                arcSpeed = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), arcSpeed, 0.0f, 2.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Radius");
                radius = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), radius, 0.2f, 5.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Radius Thickness");
                radiusThickness = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), radiusThickness, 0.0f, 1.0f);
                y += spacing;
            }  
      
            if (shapeType == [ParticleSystemShapeType.SingleSidedEdge](ParticleSystemShapeType.SingleSidedEdge.html))
            {
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Radius");
                radius = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), radius, 0.2f, 5.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Radius [Mode](Scripting.GarbageCollector.Mode.html)");
                radiusMode = ([ParticleSystemShapeMultiModeValue](ParticleSystemShapeMultiModeValue.html))[GUI.SelectionGrid](GUI.SelectionGrid.html)(new [Rect](Rect.html)(165, y, 360, 20), (int)radiusMode, new [GUIContent](GUIContent.html)[] { new [GUIContent](GUIContent.html)("[Random](Random.html)"), new [GUIContent](GUIContent.html)("Loop"), new [GUIContent](GUIContent.html)("[Ping](Ping.html)-Pong"), new [GUIContent](GUIContent.html)("[Burst](ParticleSystem.Burst.html) Spread") }, 4);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Radius Spread");
                radiusSpread = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), radiusSpread, 0.0f, 1.0f);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Radius Speed");
                radiusSpeed = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), radiusSpeed, 0.0f, 2.0f);
                y += spacing;
            }  
      
            if (shapeType == [ParticleSystemShapeType.Mesh](ParticleSystemShapeType.Mesh.html) || shapeType == [ParticleSystemShapeType.Sprite](ParticleSystemShapeType.Sprite.html))
            {
                meshShapeType = ([ParticleSystemMeshShapeType](ParticleSystemMeshShapeType.html))[GUI.SelectionGrid](GUI.SelectionGrid.html)(new [Rect](Rect.html)(25, y + 5, 300, 20), (int)meshShapeType, new [GUIContent](GUIContent.html)[] { new [GUIContent](GUIContent.html)("[Vertex](UIElements.Vertex.html)"), new [GUIContent](GUIContent.html)("[Edge](RectTransform.Edge.html)"), new [GUIContent](GUIContent.html)("Polygon") }, 3);
                y += spacing;  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Normal Offset");
                normalOffset = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), normalOffset, -3.0f, 3.0f);
                y += spacing;
            }  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Randomize [Direction](UIElements.NavigationMoveEvent.Direction.html)");
            randomizeDirection = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), randomizeDirection, 0.0f, 1.0f);
            y += spacing;  
      
            if (shapeType != [ParticleSystemShapeType.Sphere](ParticleSystemShapeType.Sphere.html))
            {
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Spherize [Direction](UIElements.NavigationMoveEvent.Direction.html)");
                spherizeDirection = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), spherizeDirection, 0.0f, 1.0f);
                y += spacing;
            }  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Randomize [Position](UIElements.Position.html)");
            randomizePosition = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), randomizePosition, 0.0f, 1.0f);
            y += spacing;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "[Position](UIElements.Position.html)");
            position.x = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 50, 30), position.x, -2.0f, 2.0f);
            position.y = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(220, y + 5, 50, 30), position.y, -2.0f, 2.0f);
            position.z = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(275, y + 5, 50, 30), position.z, -2.0f, 2.0f);
            y += spacing;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Rotation");
            rotation.x = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 50, 30), rotation.x, 0.0f, 360.0f);
            rotation.y = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(220, y + 5, 50, 30), rotation.y, 0.0f, 360.0f);
            rotation.z = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(275, y + 5, 50, 30), rotation.z, 0.0f, 360.0f);
            y += spacing;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "[Scale](UIElements.Scale.html)");
            scale.x = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 50, 30), scale.x, 0.0f, 3.0f);
            scale.y = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(220, y + 5, 50, 30), scale.y, 0.0f, 3.0f);
            scale.z = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(275, y + 5, 50, 30), scale.z, 0.0f, 3.0f);
            y += spacing;
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

